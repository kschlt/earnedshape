# CP-11 — Unified Hypothesis Register

> **Published record of change proposal CP-11** (see [`docs/review/disposition.md`](../docs/review/disposition.md)). Status unchanged: a proposal; nothing in `protocol/` has been renamed yet. The legacy IDs in the fifth column come from the two unpublished evidence cases and the protocol files; [`docs/provenance.md`](../docs/provenance.md) explains them. `phase0/capabilities/catalogue.md` is now [`capabilities/catalogue.md`](../capabilities/catalogue.md).

> **Executes:** the second half of change proposal CP-11, addressing the ID sprawl recorded in `09` §2.2: the same claims currently carry different identifiers in five places — `H-01..H-12` (Case 02 §15), `H-SL-01` (Case 02A), `E1..E10` (`protocol/05` §10), `P-01..P-14` / `E-01..E-08` / `T-01..T-13` (`protocol/07`; *added on publication:* `T-11..T-13` were proposed in the adversarial review), and `M-01..M-12` (Case 01). A reader cannot tell whether two IDs are one claim. *(As of v0.2. In v0.2.1, `P-15` was added and `T-01..T-10` moved to [`docs/technical-decisions.md`](../docs/technical-decisions.md).)*
> **Status:** proposal. Nothing renamed in `protocol/` yet.

## Structure

One ID space, `HYP-nnn`, immutable once allocated. Three kinds, because they were being mixed:

- **hypothesis** — a testable claim about what improves discovery
- **question** — genuinely open, not yet a claim
- **decided** — adopted as a protocol decision; listed so its evidential basis stays visible

The `evidence` column is the honest one: it says what the claim actually rests on, not how confident the prose sounds.

## Register

| ID | Claim | Kind | Evidence today | Legacy IDs | Capability | Testable now? |
|---|---|---|---|---|---|---|
| HYP-001 | An incomplete, explicitly provisional model elicits more correction than a polished one | hypothesis | both cases, dependent | H-01, E1, M-01, L2/L3 (Case 01) | — | yes, needs `turn.recorded` |
| HYP-002 | Capturing an independent human position before strong AI output preserves information that would otherwise be lost | hypothesis | timing studies, adjacent task | H-02, E2 | CAP-14 | only if the trigger is an enumerated list (CP-03) |
| HYP-003 | Explicit probe labelling plus a debrief beats natural reflection | hypothesis | not tested | H-03, E3, HYP-02/03 (Case 02) | CAP-13 | yes |
| HYP-004 | Research should produce an explicit model delta | **decided** | D-20; Case 01 M-09 kept | H-04, M-09 | CAP-12 | — |
| HYP-005 | Importing a prior framework requires an explicit non-transferability analysis | **decided** | D-19; one observed failure (Turn) | H-05, E8 | CAP-15 | exercised in CP-09 |
| HYP-006 | Initiative is a per-move property, not a role | **decided** | D-06; observed in both cases | H-06 | — | — |
| HYP-007 | A five-factor router allocates initiative well | hypothesis | never exercised | H-07 | none — deliberately | **no** — no event would show it fired |
| HYP-008 | Persistent external state beats strong implicit memory | hypothesis | need observed, effect untested | H-08, E4 | CAP-01 | yes |
| HYP-009 | Compact navigation turns beat repeated long synthesis | hypothesis | one case, contradicted in execution | H-09, E9 | — | **only if** `turn.recorded` is reachable |
| HYP-010 | Handoff with explicit deferrals beats more exhaustive discovery | hypothesis | one case | H-10, E10, M-12 | CAP-05, CAP-09 | yes |
| HYP-011 | A whole-baseline adversarial review before release catches what the pair normalized | **decided** | D-21; its absence was the defect | H-11 | CAP-10 | — |
| HYP-012 | Public context known early changes artifacts for the better | **decided** | D-13, `06` §6; M-11 | H-12, M-11 | — | — |
| HYP-013 | Model-bearing AI terms treated as candidates surface disagreement earlier | hypothesis | mechanism plausible, causality absent | H-SL-01, E5 | CAP-11 | yes |
| HYP-014 | Meaning-first selective terminology work pays for its interaction cost | hypothesis | untested | E6 | CAP-11 | yes |
| HYP-015 | Preserving the human source expression beside the AI reformulation reveals drift | hypothesis | untested | E7 | CAP-11 | yes |
| HYP-016 | The human's counterexamples are worth more than the human's solutions | **decided without test** | Case 01 hypothesis, promoted in v0.2 | M-07 | — | reopen? see note |
| HYP-017 | An explicit decision horizon reduces overdesign | **decided without test** | Case 01 hypothesis, promoted | M-08 | CAP-05 | reopen? see note |
| HYP-018 | Artifact version churn degrades discovery past a point | **decided without test** | Case 01 hypothesis, promoted | M-10 | — | reopen? see note |
| HYP-019 | Adversarial review is most valuable while the model is still cheap to change | hypothesis | **dropped from v0.2**; back in the protocol text in v0.2.1 (CP-20), untested | M-02, G6 | CAP-10 | yes — CP-20 |
| HYP-020 | Broad falsification then narrow verification converges better than one large review | hypothesis | **dropped from v0.2**; back in the protocol text in v0.2.1 (CP-16), untested | M-03, M7, EV-4 | CAP-10 | yes — CP-16 |
| HYP-021 | Real counterexamples produce better models than feature brainstorming | hypothesis | **dropped from v0.2**; back in the protocol text in v0.2.1 (CP-21), untested | M-04 | — | yes — CP-21 |
| HYP-022 | Source / canonical / derived separation is a generalizable AI-discovery pattern | hypothesis | **dropped from v0.2**; back in the protocol text in v0.2.1 (CP-18), untested | M-05, G3, L3, L7 | CAP-16 | yes — CP-18 |
| HYP-023 | A future-readiness check prevents irreversible information loss | hypothesis | **dropped from v0.2**; back in the protocol text in v0.2.1 (CP-18), untested | M-06, AP-05 | CAP-16 | yes — CP-18 |
| HYP-024 | An in-session halt heuristic prevents unproductive continuation | hypothesis | **dropped from v0.2**; back in the protocol text in v0.2.1 (CP-17), untested | SC-3, AP-09 | — | yes — CP-17 |
| HYP-025 | Recorded dissent predicts later reopenings | hypothesis | new, from CP-05 | — | CAP-06 | yes — the one predictive test available at n=1 |

Open **questions** (`P-01..P-15`, `E-01..E-08`) and deferred **technical decisions** (`T-01..T-13`: `T-01..T-10` in [`docs/technical-decisions.md`](../docs/technical-decisions.md), section B of `protocol/07` up to v0.2; `T-11..T-13` proposed in the adversarial review) keep their existing IDs and are not folded in: they are not claims, and merging them would recreate the confusion this register removes. `07` should link here rather than restate.

## Three findings from building it

**1. Three claims were promoted from hypothesis to decision without a test.** HYP-016, 017 and 018 were open questions in Case 01's learning backlog and are settled model in v0.2, on the evidence of one dependent case. They are not wrong — they are plausible and probably right — but they are marked `decided` on the same evidential basis that other claims are marked `experimental`, and nothing records why they were treated differently.

**2. One hypothesis is untestable as specified, and that is worth saying out loud.** HYP-007, the five-factor router, has no event that would show it fired, because it describes a judgement rather than an act. `phase0/capabilities/catalogue.md` deliberately defines no capability for it. Either it becomes an act that leaves a trace, or it should be marked untestable in the protocol rather than sitting in the list looking like a mechanism awaiting evidence.

**3. Two hypotheses depend on one unresolved technical question.** HYP-001 and HYP-009 both need `turn.recorded`. If Phase 1 finds conversational turns unreachable, both are unmeasurable in this project — and HYP-001 is the criticism-surface claim, which is the single most-cited mechanism in both evidence cases. That dependency deserves to be visible before the spike, not discovered after it.
