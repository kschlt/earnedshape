# Run Record

> **Status:** experimental, protocol v0.2.1. Rules may still change between versions.

> **Owns:** what a discovery run is, how it is identified, and the metadata without which two runs cannot honestly be compared.

## What a run is

A **run** is one bounded discovery effort with a single object of discovery, from first framing to handoff or abandonment. It is not a session: a run normally spans several sessions, and a session may contain no run at all.

Two consequences:

- **A run must be declared.** Not every session is observed — only those the practitioner enrols. An unenrolled session produces no run evidence, and that is correct behaviour, not a gap.
- **A run survives the session boundary.** Its identity, state and event stream outlive any one conversation, which is the whole reason external state exists.

## Identity

```
run_id: <YYYY-MM-DD>-<short random>      # e.g. 2026-09-10-a7f3
```

Date-prefixed and sortable, random suffix so two runs on one day never collide, short enough to type. Deliberately **not** derived from the project, the repo or the domain: the run id appears in sanitized findings that leave the private store, and it must reveal nothing.

## Record

```yaml
run_id:
started_at:                 # RFC3339 UTC
ended_at:                   # null while active

# what is being discovered
domain:                     # free text, private
object_type:                # product | internal-tool | method | research | other
prior_art:                  # none | continues <run_id> | reanalysis-of <run_id>

# where it ran
surface:                    # claude-code | claude-chat | chatgpt-chat | chatgpt-project | other
model_family:               # claude | gpt | other
model_id:                   # as reported by the surface, verbatim
harness_version:            # if the surface reports one

# what was in force
protocol_version:
observation_version:        # this model's version; a change here breaks comparability
adapter:                    # name, or none
adapter_version:
capabilities_active:        # [] for a baseline run
  - id: CAP-04
    level: L2               # the enforcement level actually in force, per capability
blank_start: true|false     # no protocol tooling of any kind

# how well it was observed
fidelity:                   # auto | semi | manual — see 03-fidelity-levels.md
fidelity_notes:             # what was lost, if known

# who
practitioner:               # stable pseudonymous id
practitioner_prior_runs:    # integer — the learning confound, recorded not corrected

# what came of it
outcome_status:             # active | handed-off | abandoned | superseded
handoff_ref:                # pointer into the private store
project_ref:                # the thing that got built, if any — makes rework questions answerable later
```

## Why these fields and not fewer

Everything above `fidelity` exists so that a later comparison can be interpreted at all. Four of them are the confounders that would otherwise be invisible:

- **`capabilities_active` with per-capability level.** Two runs "with the protocol" are not the same treatment if one had a capability at L1 guidance and the other at L3 enforcement. Without the level, every combination effect is uninterpretable.
- **`model_family` / `model_id`.** The protocol's central risk claim — fluency becoming unnoticed commitment — is a claim about model behaviour. A change of model family is a change of treatment, not a change of tooling.
- **`observation_version`.** A change to the event vocabulary silently redefines every count derived from it. Runs across a version boundary are not comparable without an explicit migration note.
- **`practitioner_prior_runs`.** The practitioner gets better at discovery independently of the protocol. This cannot be corrected for at n=1; it can be recorded, so that a trend is at least visible as ambiguous rather than read as an effect.

`blank_start` is what makes a baseline identifiable years later, when nobody remembers which runs were untreated.

## What must be true

1. A run record exists before the first event of that run, or the run is not observed.
2. `capabilities_active` reflects what was **in force**, not what was installed. If a capability was present but disabled, it is not listed.
3. `fidelity` is assigned by the adapter, never by the practitioner's impression.
4. A field that is unknown is written as `unknown`, never omitted and never guessed. An omitted field and an unknown one mean different things downstream.
