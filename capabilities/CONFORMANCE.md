# Conformance Matrix

> **Owns:** per surface, which capabilities are realized, by what mechanism, and whether their effect is observable.
> **Status:** Honestly empty. Every `?` is a question for the Phase 1 feasibility spikes. A filled-in guess here would be the most expensive kind of wrong.

## How to read it

Three separate questions per cell, never collapsed:

- **realized** — is it implemented in this surface at all
- **level** — at which enforcement level (L0 text · L1 guidance · L2 skill · L3 deterministic)
- **observable** — can its firing be recorded, and at what fidelity (auto · semi · manual · no)

> **An empty `observable` cell is a hard gate: no evaluation claim may be made about that capability in that surface.** Not a weaker claim — none.

## Matrix

| Capability | Core? | Class | CC: realized | CC: level | CC: observable | GPT: realized | GPT: level | GPT: observable |
|---|---|---|---|---|---|---|---|---|
| CAP-01 persistent state | core | enf | ? | ? | ? | ? | ? | ? |
| CAP-02 run observation | core | obs | ? | ? | ? | ? | ? | ? |
| CAP-03 status transitions | core | enf | ? | ? | ? | ? | ? | ? |
| CAP-04 commitment act | core | enf | ? | ? | ? | ? | ? | ? |
| CAP-05 deferral register | core | enf | ? | ? | ? | ? | ? | ? |
| CAP-06 recorded challenge | core | enf | ? | ? | ? | ? | ? | ? |
| CAP-07 epistemic separation | core | enf | ? | ? | ? | ? | ? | ? |
| CAP-09 handoff + cold start | core | enf | ? | ? | ? | ? | ? | ? |
| CAP-10 adversarial gate | core | enf | ? | ? | ? | ? | ? | ? |
| CAP-08 contradiction surfacing | ext | enf | ? | ? | ? | ? | ? | ? |
| CAP-11 concept entry | ext | enf | ? | ? | ? | ? | ? | ? |
| CAP-12 research delta | ext | enf | ? | ? | ? | ? | ? | ? |
| CAP-13 probe + debrief | ext | enf | ? | ? | ? | ? | ? | ? |
| CAP-14 independent position | ext | enf | ? | ? | ? | ? | ? | ? |
| CAP-15 analogy record | ext | enf | ? | ? | ? | ? | ? | ? |

`CC` = Claude Code · `GPT` = a ChatGPT surface, which one to be decided.

## Event reachability — the prior question

The matrix above cannot be filled before this one is, because a capability's observability is the conjunction of its events' reachability.

| Event kind | Required? | CC | GPT | Note |
|---|---|---|---|---|
| `run.started` / `run.ended` | yes | ? | ? | needs an enrolment mechanism in both |
| `turn.recorded` | yes | ? | ? | **the decisive unknown** — existing hook precedents capture tool calls, not conversational turns |
| `object.created` / `object.status_changed` | yes | ? | ? | plausible via a state file write in a surface with a filesystem |
| `commitment.recorded` | yes | ? | ? | |
| `deferral.recorded` / `.resolved` | yes | ? | ? | |
| `challenge.raised` / `.resolved` | yes | ? | ? | |
| `capability.exposed` / `.invoked` | yes | ? | ? | without these, evaluation level 1 does not exist |
| `capability.skipped` | yes | ? | ? | reliably emittable only at L3 |
| extended kinds | no | ? | ? | |

## What Phase 1 must produce

For each cell, one of: a working demonstration, a demonstrated impossibility, or a named cost. Not an opinion.

Two outputs fall out of the completed matrix and are worth stating in advance, because they are the point of building it:

1. **Surface fitness.** "Run discoveries that depend on CAP-04 in the surface where it reaches L3" is a real recommendation derived from data, not a preference.
2. **A demotion list.** Any hypothesis whose capability is unobservable in every available surface is not testable now, and should be marked as such in the protocol rather than left looking like a mechanism in waiting.
