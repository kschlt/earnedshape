# Changelog

Protocol versions are recorded here with the changed rule, the observation that motivated it, and what remains hypothesis (`protocol/06` §9). Repository changes that do not change the protocol are not listed.

## Unreleased

## v0.2.1 — consolidation of accepted change proposals (not yet tagged)

v0.2.1 applies the change proposals that were accepted but not yet in the protocol text. It adds no proposal of its own; each change traces to one proposal, and [`docs/review/disposition.md`](docs/review/disposition.md) records where each landed. File names are unchanged; headings and status lines read v0.2.1.

| Proposal | Changed rule | Observation that motivated it | Still hypothesis |
|---|---|---|---|
| CP-01 | `01` §13: convergence requires the model to have survived one deliberate attempt to break it, by a party or context independent of the pair that built it; a review typology (exploration, adversarial, verification, spike); §15 is the release instance of the same mechanism | review finding F-02; Case 01's broad-review-then-narrow-verification sequence | whether findings are material rather than cosmetic (`CAP-10`) |
| CP-02 | `01` §5, `02` §1: a mode names the dominant learning objective of the moment, never a phase (option b; names unchanged) | finding F-01: the mode names separated problem and solution, which `01` §7 forbids | — |
| CP-04 | `01` §3: Progressive Commitment is the one tentativeness ladder, with one presentation rule; §6 becomes guidance; `02` §7 is its state encoding | finding F-07: four overlapping tentativeness devices | — |
| CP-08 | `05` §12: one evidence-strength scale, split into observation clarity and evidential weight | finding F-11: two incompatible evidence-strength vocabularies | the scale values are a first definition |
| CP-13 | `05` §2, §3, §9, §11: pre-registered predictions (at most five per case) are the primary instrument; three always-on measures; the other signals are optional diagnostics; Keep/Investigate/Revert over predictions | findings F-09 (evaluation cannot run at the available sample size), F-13 | whether the three always-on measures predict rework |
| CP-14 | `01` §1: declared scope (one human, one AI, single-threaded, ending in a handoff) and known untested extensions | findings F-14, F-16, F-21 | everything outside the declared scope |
| CP-16 | `01` §13: the review's return leg — fix named blockers, resolution log, narrow verification, ready/not-ready verdict | Case 01's convergence record | whether the return leg shortens convergence |
| CP-17 | `01` §13: an in-session stop signal with five symptoms | Case 01's premature "we're done" moments | whether the symptoms are noticed in time |
| CP-18 | `01` §9: information-loss check before any irreversible normalization; `CAP-16`; extended event kind `normalization.recorded` | Case 01: the terminology rule's general form | whether recorded losses are ever needed again (`CAP-16`) |
| CP-19 | `01` §11: reuse check for borrowed components before architecture | Case 01 G1, EV-1: nothing covered borrowed components, only borrowed ideas | — |
| CP-20 | `01` §13: review when the model is coherent, attackable and still cheap to change; the timing question reinstated as `07` P-15 | v0.2 moved the trigger to release without a stated reason | P-15 itself |
| CP-21 | `01` §12: counterexamples classified local or structural; saturation when new ones cause mostly local changes | Case 01's counterexample method, dropped in v0.2 | whether saturation predicts a stable model |
| CP-22 | `07` section B (deferred technical decisions `T-01`–`T-10`) moved to [`docs/technical-decisions.md`](docs/technical-decisions.md); `T-01` marked decided | known finding KF-2: project decisions in the normative layer, and the only reason it named a harness | — |

**Observation model.** One extended event kind, `normalization.recorded`, is added. Under the vocabulary's own rule a new kind is a version bump; this is it, and it is the migration note. No run has been recorded yet, so no comparability is lost.

**What did not happen.** The adversarial review's own plan for v0.2.1 (its §7, W1) expected a *smaller* normative document. This consolidation is larger: CP-16 to CP-21 add mechanisms that Case 01 had and v0.2 dropped, and none of them is tested yet. CP-15 remains deferred. KF-1 and KF-3 remain open. The Core/Extended split (CP-11) is still a proposal in the catalogue, not a protocol decision.
- Research references checked against publisher and index records, with unconfirmed fields marked; review record, change-proposal disposition, hypothesis register and analogy records published (see `docs/review/`, `research/`).

---

## v0.2 — from v0.1

The section below is the change record written when v0.2 was produced, kept as written. "This package" refers to the private working package the repository was derived from; see [`docs/provenance.md`](docs/provenance.md).

### Why v0.2 exists

v0.1 was intentionally packaged once the conceptual discovery had reached a coherent baseline.

Two later inputs materially changed that baseline:

1. a full meta-retrospective of the session that created v0.1;
2. focused research on Shared Conceptual Language and AI terminology anchoring.

The changes below are therefore treated as a genuine protocol revision, not an appendix-only documentation update.

---

### 1. New core principle — Progressive Commitment

v0.1 already distinguished:

`PROBE ≠ CANDIDATE ≠ RECOMMENDATION ≠ DECISION ≠ COMMITMENT`

v0.2 generalizes the underlying mechanism:

> **AI may externalize tentative structure early, but the protocol must preserve the distinction between a useful proposal and an accepted model commitment.**

This applies not only to solutions.

It also applies to:

- problem frames,
- conceptual models,
- terminology,
- interpretations,
- research-derived hypotheses,
- recommendations,
- downstream decisions.

Examples:

```text
Candidate term → Working term → Canonical-for-now

Solution probe → Candidate → Recommendation → Decision → Commitment

Working frame → Accepted frame for current decision horizon
```

---

### 2. Shared Language becomes first-class

New normative concern:

> **Shared conceptual language should be negotiated progressively, not silently normalized by AI.**

v0.2 adds `protocol/04_SHARED_LANGUAGE_POLICY.md`.

Key changes:

- human source meaning may need to be preserved;
- AI-generated model-bearing terms begin as proposals;
- unresolved consequential ambiguity should trigger semantic clarification;
- candidate terminology can be used as a semantic probe;
- important terms should be tested in actual scenarios/use before stabilization;
- "canonical" means `canonical-for-now-and-context`;
- terms may be reopened, split, merged, renamed or deprecated;
- no mandatory full glossary or separate terminology phase is introduced.

---

### 3. `Meaning before naming` → `Meaning before commitment`

The research challenged a strict rule that AI must delay naming until a concept is already fully understood.

Early labels can help articulation, memory, distinction-making and reasoning.

The revised rule is:

> **Early naming is allowed. Early implicit model commitment is not.**

---

### 4. Human Contribution Model retained, with one refinement

The five current human contributions remain:

1. Situated Grounding
2. Framing & Meaning
3. Independent Position / Authorship
4. Judgment & Exceptions
5. Commitment & Accountability

Shared Language is **not** a sixth contribution.

It is a cross-cutting coordination mechanism connecting these contributions to shared state and later handoff.

`Independent Position / Authorship` now explicitly includes **framing-bearing terminology** where AI naming could erase a useful human distinction.

---

### 5. State model expanded

The working state may now maintain lightweight `concepts` / `shared_language` entries for model-relevant language.

Minimum candidate fields:

- current term,
- meaning,
- status,
- context,
- optional human source expression,
- example/boundary,
- optional provenance,
- open issue,
- meaningful rename history.

This is intentionally selective.

The trigger is not "new word".

The trigger is:

> **Would a different interpretation change requirements, decisions, boundaries, responsibilities, priorities or handoff meaning?**

---

### 6. New interaction distinction — structure for exploration vs convergence

Evidence Case 02 showed that AI structure has two different roles:

#### Structure for exploration
- provisional,
- explicitly criticizable,
- exposes assumptions,
- invites counterexamples,
- can be replaced cheaply.

#### Structure for convergence
- consolidates evidence,
- compares alternatives,
- stabilizes current decisions,
- can become a reference baseline.

The protocol should not render an exploratory structure with the rhetorical certainty of a converged model.

---

### 7. New Analogy Boundary Check

Evidence Case 02 showed a failure mode when the prior `Turn` model was initially mapped too directly onto Discovery.

Whenever a prior framework, architecture, product or methodology is imported as precedent, v0.2 now requires a lightweight check:

1. What original problem did it solve?
2. What is genuinely similar?
3. What important assumptions differ?
4. What mechanisms transfer?
5. What must explicitly not transfer?

---

### 8. Research now produces Model Delta

After focused research, the discovery should not stop at "here is what the literature says".

Record what changed:

- `REINFORCED`
- `REFINED`
- `CHALLENGED`
- `NEW`
- `NO CHANGE`

Also record:
- what became more uncertain;
- what decision became possible;
- what hypothesis should remain experimental.

---

### 9. Final stable/public baseline needs whole-package adversarial review

v0.1 was packaged after focused research but without one independent adversarial review of the whole protocol.

v0.2 adds this as a pre-release recommendation:

- contradiction search,
- evidence/overclaiming review,
- missing-boundary review,
- handoff fitness test,
- public-source/citation review.

---

### 10. Evidence architecture improved

This package now separates:

- normative protocol;
- curated research synthesis;
- retrospective evidence cases;
- raw research inputs.

This separation is important for later cumulative method development.

A claim in a normative file is not evidence for itself.
