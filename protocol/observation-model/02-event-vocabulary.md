# Event Vocabulary

> **Status:** experimental, protocol v0.2. Rules may still change between versions.

> **Owns:** the envelope every event carries, the event kinds, and which subset is required for a conformant run.

## Envelope

Every event, regardless of kind:

```yaml
event_id:                   # unique, sortable
run_id:
seq:                        # monotonic within the run, gaps are a defect
ts:                         # RFC3339 UTC
schema_version:             # observation model version
kind:                       # from the tables below
source:                     # auto | model | human   — HOW this event was captured
actor:                      # human | ai | external | system  — WHO acted
capability_id:              # optional; set when the event was produced under a capability
payload:                    # kind-specific, see below
```

**`source` is the field most systems omit and then regret.** Fidelity is not only a property of a run — it varies per event. A `commitment.recorded` written deterministically by a hook (`source: auto`) and one the model emitted because it was asked nicely (`source: model`) are different evidence. A later analysis that cannot tell them apart will read compliance where it should read self-report.

**`actor` is not `source`.** A human's decision captured automatically is `actor: human, source: auto`. Conflating them loses both the provenance and the reliability.

## Required kinds

A run is conformant only if these can appear. Everything in the next section is extended.

### Session frame

| kind | payload | note |
|---|---|---|
| `run.started` | snapshot of the run record | must be the first event |
| `run.ended` | `outcome_status` | absence means the run is active or the observation broke — distinguishable only by `ts` age |
| `turn.recorded` | `ordinal`, `actor`, `length_class`, `summary_ref` | see the warning below |

> **`turn.recorded` is the known hard one.** The closest existing hook-based tooling precedent captures *tool calls*, not conversational turns — and for discovery, the conversation is most of what matters. Whether a turn is observable at all, in either surface, is the single most important question Phase 1 must answer. If it is not, several hypotheses (turn economics, elicit-before-generate, criticism surface) become unmeasurable and should be demoted rather than quietly assumed. <!-- lint:vendor-ok -->

### Discovery objects

| kind | payload |
|---|---|
| `object.created` | `object_id`, `object_type`, `status`, `summary_ref` |
| `object.status_changed` | `object_id`, `from`, `to`, `rationale_ref` |
| `object.superseded` | `object_id`, `superseded_by` |
| `commitment.recorded` | `object_id`, `owner`, `rejected_alternative`, `rationale_ref`, `evidence_refs`, `revisit_condition` |
| `deferral.recorded` | `question_id`, `reason`, `decision_point` |
| `deferral.resolved` | `question_id`, `resolution_ref` |

`object_type` ∈ `frame · probe · candidate · recommendation · decision · commitment · question · assumption · constraint`.

`commitment.recorded` is deliberately not just a status change to `commitment`. The protocol's whole defence against silent commitment is that a commitment carries a rejected alternative and a revisit condition; an event that cannot carry them cannot enforce it.

### Disagreement

| kind | payload |
|---|---|
| `challenge.raised` | `challenge_id`, `by` (`ai`\|`human`\|`external`), `target_object`, `summary_ref` |
| `challenge.resolved` | `challenge_id`, `resolution` (`accepted`\|`overruled`\|`deferred`\|`unresolved`) |

Required, because a two-party discovery has no other defence against friendly consensus, and because an unresolved challenge at handoff is a fact the receiving context needs.

### Capability meta

| kind | payload |
|---|---|
| `capability.exposed` | `capability_id`, `level`, `surface` |
| `capability.invoked` | `capability_id`, `level`, `trigger` |
| `capability.skipped` | `capability_id`, `reason`, `detected_by` |

**Exposed is not invoked.** A capability that was available and never fired is the most common cause of a null result being misread as "the method does not work". These three kinds are what makes evaluation level 1 computable at all; without them, level 2 is uninterpretable.

`capability.skipped` is only reliably emittable at L3, where something deterministic notices. At L1 and L2 it is usually reconstructed in later analysis, and should then carry `detected_by: analysis`.

## Extended kinds

Not required for conformance. Each corresponds to a mechanism the protocol currently treats as a hypothesis, and each exists so the hypothesis can be tested rather than asserted.

| kind | payload | tests |
|---|---|---|
| `epistemic.recorded` | `claim_id`, `status`, `statement_ref` | evidence/inference separation |
| `epistemic.status_changed` | `claim_id`, `from`, `to` | stale assumption detection |
| `concept.introduced` | `concept_id`, `term`, `status`, `provenance`, `source_expression_ref` | candidate-first terminology |
| `concept.status_changed` | `concept_id`, `from`, `to` | the shared-language lifecycle |
| `concept.tested_in_use` | `concept_id`, `scenario_ref`, `outcome` | the scenario gate |
| `research.delta_recorded` | `question`, `result`, `decision_impact`, `new_uncertainty` | research model delta |
| `analogy.recorded` | `source`, `original_problem`, `transferable`, `non_transferable` | analogy boundary check |
| `normalization.recorded` | `discarded`, `reconstruction_cost` | information-loss check before normalization |
| `human_position.elicited` | `trigger`, `contribution_type`, `before_ai_output` | the human-first signal |
| `probe.debriefed` | `probe_id`, `learning_ref`, `assumption_changed`, `disposition` | probe debrief |
| `adversarial_review.completed` | `scope`, `reviewer_kind`, `findings`, `blocking` | the adversarial gate |
| `handoff.produced` | `artifact_ref` | readiness |
| `coldstart.tested` | `blockers`, `max_severity`, `tested_by` | handoff fitness |

## Rules

1. **Events are append-only.** A correction is a new event, never an edit. The record of having got it wrong is itself evidence.
2. **`seq` gaps are defects**, not noise — they mean the observer dropped something, and a run with gaps must not be used for frequency comparisons.
3. **Every required kind must be emittable by any conformant adapter**, at whatever fidelity the surface allows. "We could not capture it" is a fidelity statement, not an exemption.
4. **A new kind is a version bump** of the observation model, and breaks comparability with earlier runs unless a migration note says otherwise.
5. **Payloads carry references, not content** — see `04-recording-boundaries.md`.
