# Provenance — where this material comes from

This repository was derived on 14 September 2026 from a private working repository in which the protocol was developed. Some files here refer to documents, identifiers and projects from that repository. This page says what they are, so a reference is at least understandable where it cannot be followed.

## How the protocol came about

| When | What | Published here? |
|---|---|---|
| before Sep 2026 | **Case 01** — a long product discovery with an AI (the recipe tool [Cookframe](https://github.com/kschlt/cookframe)), analysed retrospectively afterwards | no — see below |
| up to 5 Sep 2026 | **Case 02** — a second discovery whose subject was human–AI discovery itself, using Case 01's retrospective as input. It produced protocol v0.1 | no |
| | Four focused research reports: human contribution and interaction design; problem framing, solution probes and fixation; evaluating a discovery protocol; shared conceptual language | as a synthesis in [`research/`](../research/), with checked sources in [`research/REFERENCES.md`](../research/REFERENCES.md) |
| 5 Sep 2026 | **Protocol v0.2**, after a post-hoc shared-language addendum to Case 02 | [`protocol/`](../protocol/), [`CHANGELOG.md`](../CHANGELOG.md) |
| 10 Sep 2026 | Orientation and **adversarial review** of v0.2: 25 findings, 15 change proposals | [`docs/review/`](review/) |
| 10–14 Sep 2026 | **Phase 0**: observation model, capability catalogue, conformance matrix, boundary lint; four change proposals executed | [`protocol/observation-model/`](../protocol/observation-model/), [`capabilities/`](../capabilities/), [`research/hypothesis-register.md`](../research/hypothesis-register.md), [`research/analogy-records.md`](../research/analogy-records.md) |
| 14 Sep 2026 | Name decided, this repository derived | [`examples/naming-decision.md`](../examples/naming-decision.md) |
| from 14 Sep 2026 | **Phase 1** planned: feasibility spikes on what can be observed | [`docs/phase-1-feasibility.md`](phase-1-feasibility.md) |
| 22 Sep 2026 | **Protocol v0.2.1**: the accepted change proposals applied to the protocol text | [`CHANGELOG.md`](../CHANGELOG.md), [`docs/review/disposition.md`](review/disposition.md) |

Cases 01 and 02 and the v0.1/v0.2 baseline were produced with ChatGPT-family models and a deep-research tool; the review and Phase 0 were done with Claude in Claude Code. The same person is practitioner, protocol author, evidence analyst and evaluator throughout — the central threat to validity the review names.

## What stays private, and why

- **The evidence cases** (Case 01, about 2,300 lines in German; Case 02 and its addendum). They are raw retrospectives and need editing for self-containedness and non-circular evidence logic before release. The synthesis in `research/` states that they are unpublished and that this limits what a reader can verify.
- **The raw research reports** (in German). They were produced with a deep-research tool and carry that tool's internal citation markers. The claims this repository relies on have been checked against publisher and index records instead; see `research/REFERENCES.md`.
- **Project-level working documents** about repository setup, naming and how this project relates to the author's other projects.

## The numbered working documents

Files here sometimes cite these by number, for example "doc 10" or `09`.

| No. | Content | Here |
|---|---|---|
| `00` | changelog v0.1 → v0.2 | [`CHANGELOG.md`](../CHANGELOG.md) |
| `08` | handover of the v0.2 package to the next agent | — |
| `09` | orientation and adversarial review of v0.2 | [`docs/review/2026-09-adversarial-review-v0.2.md`](review/2026-09-adversarial-review-v0.2.md) |
| `10` | project setup and evolution loop: the layer cut, repository layout, private run store, fidelity levels, phases | its conclusions are in [`docs/overview.md`](overview.md) |
| `11` | brief for the naming session | — |
| `12` | capability and evaluation model; reconciliation with the author's other projects | its §2 is the basis of [`capabilities/`](../capabilities/) |
| `13`–`15` | portfolio model: how the author's projects relate, what may be shared between them | — |
| `16` | status ledger and change-proposal disposition | [`docs/review/disposition.md`](review/disposition.md) |
| `17` | naming decision and move plan | [`examples/naming-decision.md`](../examples/naming-decision.md) |
| `18` | Phase 1 spike plan | [`docs/phase-1-feasibility.md`](phase-1-feasibility.md) |
| `19` | reconciliation of two parallel Phase 0 drafts | — |
| `20` | derivation record for this repository | — |

## Identifier schemes

| IDs | Meaning | Defined in |
|---|---|---|
| `D-nn`, `P-nn`, `E-nn` | protocol decisions, open protocol questions, evaluation questions | [`protocol/07`](../protocol/07_DECISIONS_AND_OPEN_QUESTIONS.md) |
| `T-nn` | deferred technical decisions (project decisions, not protocol semantics) | [`docs/technical-decisions.md`](technical-decisions.md), section B of `protocol/07` up to v0.2; `T-11`–`T-13` were proposed in the [adversarial review](review/2026-09-adversarial-review-v0.2.md) |
| `CAP-nn` | capabilities | [`capabilities/catalogue.md`](../capabilities/catalogue.md) |
| `F-nn` | findings of the adversarial review | [`docs/review/`](review/2026-09-adversarial-review-v0.2.md) §3 |
| `CP-nn` | change proposals, `CP-01`–`CP-15` from the review, `CP-16`–`CP-21` from executing CP-10, `CP-22` from known finding KF-2 | [`docs/review/disposition.md`](review/disposition.md) |
| `HYP-nnn` | unified hypothesis register | [`research/hypothesis-register.md`](../research/hypothesis-register.md) |
| `KF-n` | known findings against the published baseline | [`docs/known-findings.md`](known-findings.md) |
| `M-nn`, `M1`–`M8`, `G1`–`G7`, `L1`–`L10`, `AP-nn`, `SC-n`, `EV-n`, "Phase n" | codes inside the Case 01 retrospective: method hypotheses, method elements, guidelines, lessons, anti-patterns | unpublished |
| `E-02-nn`, `H-nn`, `HYP-0n`, `H-SL-01` | codes inside the Case 02 retrospective and its addendum | unpublished |

## The author's other projects that appear by name

Named where the protocol borrowed from them or was checked against them. Except for Cookframe they are not public at the time of writing.

- **Turn** — a design for *adaptive cognitive handoff* between a human and predominantly autonomous implementation agents. Protocol v0.1 imported its model and over-assimilated it; the analogy records trace what that import cost ([`research/analogy-records.md`](../research/analogy-records.md), A-03).
- **aos** — the author's agent workflow system for building software with Claude Code: backlog, session protocol, sealed commits, merge gate. Its hook-based telemetry was the closest existing precedent for the observation model, and it is the intended build workflow for this project's tooling.
- **loomwise** — a Claude Code plugin for human-governed knowledge development ("the AI proposes; the human owns"); the precedent for plugin packaging and behavioural evaluation.
- **CWS** — a project that observes work across projects and proposes methods and tools from it; related in scope, deliberately kept independent of this one.
- **Methodplane** — the umbrella under which these projects may eventually be published together.
- **Cookframe** — the product of the Case 01 discovery: [github.com/kschlt/cookframe](https://github.com/kschlt/cookframe).
