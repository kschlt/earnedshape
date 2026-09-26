# Status Ledger & Change-Proposal Disposition

> **Published record.** The status ledger kept in the private working repository after the [adversarial review](2026-09-adversarial-review-v0.2.md), reproduced as it stood when this repository was derived (14 September 2026). It records what happened to each of the review's change proposals and to the findings they address, which is the part an outside reader cannot otherwise check. Six findings have no change proposal of their own and are not tracked in the ledger: F-04, F-06, F-12, F-15, F-20 and F-24. Of these, F-12 (no citation independently verified) has since been addressed by [`research/REFERENCES.md`](../../research/REFERENCES.md); the other five have no recorded disposition. *[Update, 22 September 2026: the rows below were updated in place for protocol v0.2.1; the git history of this file holds their earlier wording.]*
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

Doc 09 proposed CP-01..CP-15. None were applied to the protocol; that remains correct — the protocol is untouched. What follows is where each now stands. *[Update, 22 September 2026: protocol v0.2.1 applies CP-01, CP-02, CP-04, CP-08, CP-13 and CP-14 to the protocol text; the rows below say where each landed.]*

| CP | Proposal | Disposition | Where |
|---|---|---|---|
| CP-01 | adversarial challenge as a convergence gate | **accepted**; **done in v0.2.1** | drafted as `CAP-10`; protocol text in `protocol/01` §13 (challenge condition, review typology) and §15 |
| CP-02 | remove problem/solution split from mode names | **accepted** 2026-09-22 (owner, v0.2.1 consolidation); **done in v0.2.1** (option b, the proposal's low-cost option, chosen in the consolidation; modes keep their names) | `protocol/01` §5, `02` §1 |
| CP-03 | enumerated anchor-risk events instead of a self-judged trigger | **accepted** | drafted as `CAP-14`, whose L1 measurability depends on the list existing |
| CP-04 | collapse the four tentativeness devices into one ladder | **accepted** 2026-09-22 (owner, v0.2.1 consolidation); **done in v0.2.1** | `protocol/01` §3 (one ladder, one presentation rule), §6 demoted to guidance, two dimensions of `02` §7 named as its state encoding |
| CP-05 | recorded-disagreement object | **accepted** | drafted as `CAP-06` |
| CP-06 | define the commitment act | **accepted** | drafted as `CAP-04`, including the required payload |
| CP-07 | reinstate disconfirming evidence in `research/` | **done** | `research/01` §2A + correction in §2, with an amendment note recording the change |
| CP-08 | one evidence-strength scale, two columns | **accepted** 2026-09-22 (owner); **done in v0.2.1** in the protocol text | `protocol/05` §12 (one scale, observation clarity and evidential weight); `research/01` §1 points to it. Adding the second column to Case 02's ledger belongs to the unpublished evidence layer and is still outstanding there. The strength labels already in `research/` are deliberately kept as written, not mapped onto the new scale (`research/01` §1), so the harmonization the proposal asked for is only partly done |
| CP-09 | analogy records for the protocol's own four imports | **done** | `proposals/CP-09-analogy-records.md` — four records, four findings, two of them not reconstructable from the pack |
| CP-10 | Case 01 method disposition table | **done** | `proposals/CP-10-case01-method-disposition.md` — 62 elements: 26 kept, 18 transformed, 18 dropped, **0 object-level**. Six new proposals arise (CP-16..CP-21) |
| CP-11 | Core/Extended split + one hypothesis register | **done** | Core/Extended in `phase0/capabilities/catalogue.md`; register in `proposals/CP-11-hypothesis-register.md`, `HYP-001..025` over five legacy ID spaces |
| CP-12 | conformance definition + minimal trace | **executed as a draft** | `phase0/observation-model/` and `phase0/capabilities/CONFORMANCE.md` |
| CP-13 | redesign evaluation for n=1 | **accepted** 2026-09-22 (owner, v0.2.1 consolidation); **done in v0.2.1** | `protocol/05` §2 (pre-registered predictions as the primary instrument), §3 (three always-on measures, the rest an optional diagnostic catalogue), §9 (Keep/Investigate/Revert over predictions), §11 |
| CP-14 | declare the configuration assumption | **accepted** 2026-09-22 (owner, v0.2.1 consolidation); **done in v0.2.1** | `protocol/01` §1, "Declared scope" |
| CP-15 | context-scope concept status; move turn economics to binding guidance | **deferred** | `CAP-11` inherits the unresolved context-scope question and says so |

**All four outstanding accepted proposals are now done** (CP-07, CP-09, CP-10, CP-11). Five remain deferred to a v0.2.1 consolidation pass (CP-02, CP-04, CP-08, CP-13, CP-14), and executing CP-10 produced six new ones. *[Note added on publication: the table above defers six proposals, four of them to v0.2.1 (CP-02, CP-04, CP-13, CP-14) and two without a target version (CP-08, CP-15).]* *[Update, v0.2.1: CP-02, CP-04, CP-08, CP-13 and CP-14 are done; CP-15 is the only proposal from the review still deferred.]*

### New proposals from CP-10

| CP | Proposal | Priority | Disposition | Where |
|---|---|---|---|---|
| CP-16 | close the review loop: repair leg, resolution log, scoped re-review | high | **accepted** 2026-09-22 (owner); **done in v0.2.1** | `protocol/01` §13, "Closing the review loop" |
| CP-17 | an in-session stop heuristic | high | **accepted** 2026-09-22 (owner); **done in v0.2.1** | `protocol/01` §13, "Stop signal" |
| CP-18 | information-loss gate, generalized beyond terminology | high | **accepted** 2026-09-22 (owner); **done in v0.2.1** | `protocol/01` §9, "Information-loss check before normalization"; `CAP-16` specified in the catalogue (Extended); `normalization.recorded` added to the extended event kinds |
| CP-19 | reuse gate before architecture | medium | **accepted** 2026-09-22 (owner); **done in v0.2.1** | `protocol/01` §11, "Reuse check before architecture" |
| CP-20 | review timing on cost-of-change; reinstate the dropped open question | medium | **accepted** 2026-09-22 (owner); **done in v0.2.1** | `protocol/01` §13, "When to review"; open question reinstated as `07` P-15 |
| CP-21 | classify counterexamples local vs structural; define saturation | medium | **accepted** 2026-09-22 (owner); **done in v0.2.1** | `protocol/01` §12, "Counterexamples" (classification and saturation) |

All six applied in v0.2.1. CP-18 added `CAP-16` to the catalogue as an Extended capability.

### Proposals from known findings

| CP | Proposal | Disposition | Where |
|---|---|---|---|
| CP-22 | resolve known finding KF-2: move `protocol/07` section B (deferred technical decisions `T-01`–`T-10`) out of the protocol into project documentation, and mark `T-01` (project name) decided | **accepted** 2026-09-22 (owner decision to resolve KF-2 through a change proposal); **done** for v0.2.1 | [`docs/technical-decisions.md`](../technical-decisions.md); `protocol/07` keeps a one-line pointer where section B was |

CP-22 changes where the register lives, not what it says: no deferred decision other than `T-01` is decided by it, and sections A, C, D and E of `protocol/07` are unchanged by it. With section B gone, `protocol/07` no longer names a harness.

## 3. Priority findings from doc 09 §4

| Finding | Status |
|---|---|
| F-02 no adversarial gate | addressed by CP-01 → `CAP-10`; protocol text in `protocol/01` §13 since v0.2.1 |
| F-22 commitment act undefined | addressed by CP-06 → `CAP-04` |
| F-25 no conformance definition | addressed by CP-12 → phase 0, as a draft |
| F-08 no declared core | addressed by CP-11 → Core/Extended proposal in the catalogue |
| F-09 evaluation undecidable at n=1 | addressed by CP-13 in v0.2.1 (`protocol/05` §2, §3, §9); untested until a pre-registered case runs |
| F-10 / F-11 curated layer drops counter-evidence | **closed** — CP-07 applied to `research/01` |

## 4. Corrections applied after the branch review

Accepted and fixed: the missing disposition record (this file); doc 12 §5's superseded rows and §4's violation claims surviving their own premise's withdrawal; "CWS is descriptive" (its output is prescriptive — what it lacks is an a priori method); doc 14's two standards counted as earned on same-author recurrence, which is the leniency doc 09 refused the protocol; doc 11 still blocking itself and omitting CWS from the family; doc 10 §0 reinterpreting rather than overturning the T-02 deferral; `aos` eval slots are 12, not 13; the `aos` monitor hooks require an instance directory and are not usable "as-is"; loomwise's `eval-baseline` tags the materialized tree, not the tool; the Transfer Release citation; doc 14 §6 describing an impulse stream that does not exist yet; the Q5/Q6 overlap; F-02's and F-11's precision.

## 5. Two gaps the review named that are now answered

**Where Phase 0 writes.** Doc 10 §3 gives paths in a repository that does not exist. Phase 0 is drafted in `phase0/` in this repository, mirroring that layout so it moves in one piece once the project has a name and a home.

**The capability ID scheme.** Doc 10 §2's central mitigation — "the cut is enforced by a lint rule over stable IDs" — had no ID scheme anywhere. It is now `CAP-nn`, allocated in `phase0/capabilities/catalogue.md`, immutable once allocated, never reused after retirement. What the lint would check: every `CAP-nn` referenced under `adapters/**` resolves to a catalogue entry; no file under `protocol/**` names a vendor, product or harness; every Core capability appears in the conformance matrix.

## 6. Still genuinely blocking

Unchanged from doc 09 §6, and none of it blocks Phase 0 or the naming: a real, available, non-method, non-Cookframe domain for Evidence Case 03; who v1 is for; whether the model-family change is experiment or confound; what is publishable from `evidence/`.
