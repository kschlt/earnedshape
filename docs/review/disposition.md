# Status Ledger & Change-Proposal Disposition

> **Published record.** The status ledger kept in the private working repository after the [adversarial review](2026-09-adversarial-review-v0.2.md), reproduced as it stood when this repository was derived (14 September 2026). It records what happened to every finding and change proposal of that review, which is the part an outside reader cannot otherwise check.
> Paths are those of the working repository: `phase0/observation-model/` is now [`protocol/observation-model/`](../../protocol/observation-model/), `phase0/capabilities/` is now [`capabilities/`](../../capabilities/), and `proposals/CP-09…` / `proposals/CP-11…` are now [`research/analogy-records.md`](../../research/analogy-records.md) and [`research/hypothesis-register.md`](../../research/hypothesis-register.md). Numbered documents (`09`–`15`) are working documents of that repository; [`docs/provenance.md`](../provenance.md) says what each is. This is the public index of change proposals `CP-01`–`CP-21`; the current state of each is kept here from now on.

> **Status:** Live index for this branch. Update it when a document's standing changes.
> **Why it exists:** an adversarial review of this branch found that documents 10–15 dropped all fifteen change proposals from doc 09 with no record of whether each was accepted, deferred or rejected — which is precisely finding F-19's charge against Protocol v0.2 ("no file records the disposition"). The finding was correct. This file is the fix, and it is the file F-19 says v0.2 is missing.

---

## 1. Document standing

| Doc | Standing | Notes |
|---|---|---|
| `09` orientation & adversarial review | **live** | two in-place precisions added after review (F-02 scope, F-11 example) |
| `10` project setup & evolution loop | **live** | §0 now states plainly that it overturns doc 09's deferral of T-02 rather than reinterpreting it |
| `11` naming brief | **live, ready to run** | self-block removed; CWS added to the family context |
| `12` capability & eval model / CWS | **live with withdrawals** | §2 stands in full; §3 corrected for overstatement; §4's "directly violated" and "CWS is descriptive" claims withdrawn; §5's two "superseded" rows withdrawn; §6 Option C withdrawn |
| `13` portfolio model | **live** | §8's change table corrected |
| `14` methodplane-state & placement | **live with withdrawals** | §1 and §4: both proposed standards demoted from "earned" to "candidate" |
| `15` portfolio thread parked | **live** | its §6 "settled" list is scoped to design decisions, not to doc 09's findings; those are dispositioned here |
| `phase0/` | **draft, explicitly a probe** | observation model + capability catalogue + empty conformance matrix |

## 2. Change-proposal disposition

Doc 09 proposed CP-01..CP-15. None were applied to the protocol; that remains correct — the protocol is untouched. What follows is where each now stands.

| CP | Proposal | Disposition | Where |
|---|---|---|---|
| CP-01 | adversarial challenge as a convergence gate | **accepted** | drafted as `CAP-10`; protocol edit pending v0.2.1 |
| CP-02 | remove problem/solution split from mode names | **deferred to v0.2.1** | phase 0 deliberately defines no mode capability, so nothing depends on the outcome |
| CP-03 | enumerated anchor-risk events instead of a self-judged trigger | **accepted** | drafted as `CAP-14`, whose L1 measurability depends on the list existing |
| CP-04 | collapse the four tentativeness devices into one ladder | **deferred to v0.2.1** | editorial; no capability depends on it |
| CP-05 | recorded-disagreement object | **accepted** | drafted as `CAP-06` |
| CP-06 | define the commitment act | **accepted** | drafted as `CAP-04`, including the required payload |
| CP-07 | reinstate disconfirming evidence in `research/` | **done** | `research/01` §2A + correction in §2, with an amendment note recording the change |
| CP-08 | one evidence-strength scale, two columns | **deferred** | evidence-layer edit, lower urgency than the publication decision it serves |
| CP-09 | analogy records for the protocol's own four imports | **done** | `proposals/CP-09-analogy-records.md` — four records, four findings, two of them not reconstructable from the pack |
| CP-10 | Case 01 method disposition table | **done** | `proposals/CP-10-case01-method-disposition.md` — 62 elements: 26 kept, 18 transformed, 18 dropped, **0 object-level**. Six new proposals arise (CP-16..CP-21) |
| CP-11 | Core/Extended split + one hypothesis register | **done** | Core/Extended in `phase0/capabilities/catalogue.md`; register in `proposals/CP-11-hypothesis-register.md`, `HYP-001..025` over five legacy ID spaces |
| CP-12 | conformance definition + minimal trace | **executed as a draft** | `phase0/observation-model/` and `phase0/capabilities/CONFORMANCE.md` |
| CP-13 | redesign evaluation for n=1 | **deferred to v0.2.1** | phase 0 supplies the trace it would need; the redesign itself is untouched |
| CP-14 | declare the configuration assumption | **deferred to v0.2.1** | one paragraph in `protocol/01` §1 |
| CP-15 | context-scope concept status; move turn economics to binding guidance | **deferred** | `CAP-11` inherits the unresolved context-scope question and says so |

**All four outstanding accepted proposals are now done** (CP-07, CP-09, CP-10, CP-11). Five remain deferred to a v0.2.1 consolidation pass (CP-02, CP-04, CP-08, CP-13, CP-14), and executing CP-10 produced six new ones.

### New proposals from CP-10

| CP | Proposal | Priority |
|---|---|---|
| CP-16 | close the review loop: repair leg, resolution log, scoped re-review | high |
| CP-17 | an in-session stop heuristic | high |
| CP-18 | information-loss gate, generalized beyond terminology | high |
| CP-19 | reuse gate before architecture | medium |
| CP-20 | review timing on cost-of-change; reinstate the dropped open question | medium |
| CP-21 | classify counterexamples local vs structural; define saturation | medium |

None applied. CP-18 would add `CAP-16` to the catalogue.

## 3. Priority findings from doc 09 §4

| Finding | Status |
|---|---|
| F-02 no adversarial gate | addressed by CP-01 → `CAP-10`; protocol text unchanged |
| F-22 commitment act undefined | addressed by CP-06 → `CAP-04` |
| F-25 no conformance definition | addressed by CP-12 → phase 0, as a draft |
| F-08 no declared core | addressed by CP-11 → Core/Extended proposal in the catalogue |
| F-09 evaluation undecidable at n=1 | **open** — CP-13 deferred |
| F-10 / F-11 curated layer drops counter-evidence | **closed** — CP-07 applied to `research/01` |

## 4. Corrections applied after the branch review

Accepted and fixed: the missing disposition record (this file); doc 12 §5's superseded rows and §4's violation claims surviving their own premise's withdrawal; "CWS is descriptive" (its output is prescriptive — what it lacks is an a priori method); doc 14's two standards counted as earned on same-author recurrence, which is the leniency doc 09 refused the protocol; doc 11 still blocking itself and omitting CWS from the family; doc 10 §0 reinterpreting rather than overturning the T-02 deferral; `aos` eval slots are 12, not 13; the `aos` monitor hooks require an instance directory and are not usable "as-is"; loomwise's `eval-baseline` tags the materialized tree, not the tool; the Transfer Release citation; doc 14 §6 describing an impulse stream that does not exist yet; the Q5/Q6 overlap; F-02's and F-11's precision.

## 5. Two gaps the review named that are now answered

**Where Phase 0 writes.** Doc 10 §3 gives paths in a repository that does not exist. Phase 0 is drafted in `phase0/` in this repository, mirroring that layout so it moves in one piece once the project has a name and a home.

**The capability ID scheme.** Doc 10 §2's central mitigation — "the cut is enforced by a lint rule over stable IDs" — had no ID scheme anywhere. It is now `CAP-nn`, allocated in `phase0/capabilities/catalogue.md`, immutable once allocated, never reused after retirement. What the lint would check: every `CAP-nn` referenced under `adapters/**` resolves to a catalogue entry; no file under `protocol/**` names a vendor, product or harness; every Core capability appears in the conformance matrix.

## 6. Still genuinely blocking

Unchanged from doc 09 §6, and none of it blocks Phase 0 or the naming: a real, available, non-method, non-Cookframe domain for Evidence Case 03; who v1 is for; whether the model-family change is experiment or confound; what is publishable from `evidence/`.
