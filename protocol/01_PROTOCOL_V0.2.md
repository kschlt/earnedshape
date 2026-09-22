# Human–AI Discovery Protocol v0.2

> **Status:** experimental, protocol v0.2. Rules may still change between versions.

## 1. Objective

The protocol supports a human working with AI from an ambiguous starting point toward:

- grounded understanding of a problem, opportunity or workflow;
- an explicit but revisable working frame;
- a deliberately explored solution space;
- shared conceptual language where it matters;
- explicit constraints, assumptions and evidence;
- conceptual/domain/information models where needed;
- product/design principles;
- decisions and commitments;
- explicit deferred questions;
- an implementation-ready discovery baseline.

Implementation itself is a separate work mode.

---

## 2. Governing principle

> **Optimize the collaboration for the next high-value human contribution, not for the completeness of the AI's current answer.**

AI should externalize:

- retrieval,
- memory,
- state maintenance,
- transformation,
- comparison,
- evidence synthesis,
- consistency,
- variation,
- critique,
- artifact production,

where doing so does not remove valuable human cognition.

Human engagement should remain deliberate where the process depends on:

- situated evidence,
- meaning,
- independent framing,
- contextual judgment,
- normative intent,
- consequential commitment.

---

## 3. Progressive Commitment Principle

> **AI may externalize tentative structure early, but a useful proposal must remain distinguishable from an accepted model commitment.**

This principle applies across the discovery:

### Frames
`possible frame → working frame → accepted frame for current horizon`

### Language
`candidate term → working term → canonical-for-now`

### Solutions
`probe → candidate → recommendation → decision → commitment`

### Research
`finding → interpretation → model delta → accepted implication`

The protocol should resist a common LLM failure:

```text
plausible abstraction
→ polished formulation
→ repeated use
→ accidental commitment
```

Fluency is not commitment.

---

## 4. Five high-value human contributions

### 4.1 Situated Grounding

The human provides privileged access to:

- concrete episodes,
- actual workflows,
- exceptions,
- local constraints,
- stakeholder behavior,
- historical context,
- source language,
- example artifacts.

Human testimony is valuable evidence, not infallible truth.

AI should elicit concrete situations and distinguish observation from interpretation.

### 4.2 Framing & Meaning

The human helps establish:

- what matters;
- what the relevant problem/opportunity is;
- for whom;
- desired outcomes;
- intended experience;
- success criteria;
- meaningful distinctions;
- value conflicts.

Frames remain revisable when new evidence, terminology, constraints or solution insights change understanding.

### 4.3 Independent Position / Authorship

Where AI output could erase useful independent information, selectively preserve a human signal first:

- initial hypothesis,
- spontaneous interpretation,
- criterion,
- prediction,
- priority,
- preference,
- framing-bearing source language.

This is not a universal "human answers first" mandate.

The trigger is whether a strong AI anchor would destroy information worth observing.

### 4.4 Judgment & Exceptions

The human contributes:

- counterexamples,
- boundary judgments,
- contextual fit,
- quality criteria,
- exception handling,
- unacceptable simplifications,
- risk judgment.

Passive approval is not meaningful validation.

### 4.5 Commitment & Accountability

The human owns consequential commitments such as:

- vision,
- scope,
- non-goals,
- priorities,
- accepted risks,
- high-impact trade-offs,
- accepted model meanings,
- final discovery baseline.

AI may recommend and challenge. It must not silently commit on the human's behalf.

---

## 5. Discovery modes

### `PROBLEM_EXPLORATION`

Goal:
expand and improve understanding of the problem/opportunity.

AI may:
- elicit episodes;
- preserve important source expressions;
- identify evidence gaps;
- offer competing frames;
- research external questions;
- surface hidden assumptions;
- create low-commitment conceptual or solution probes.

Do not default to a single polished preferred solution.

### `SOLUTION_EXPLORATION`

Goal:
explore materially different interventions against one or more working frames.

AI may:
- vary mechanisms;
- vary actors;
- vary intervention levels;
- generate analogies;
- produce contrastive probes;
- test feasibility at appropriate granularity.

Do not confuse quantity with diversity.

### `CONVERGENCE`

Goal:
reduce the search space based on:

- explicit criteria,
- evidence,
- tested assumptions,
- scenario/boundary checks,
- accepted remaining uncertainty.

AI may:
- compare;
- challenge;
- run sensitivity analysis;
- prepare decision proposals;
- consolidate shared language;
- produce review candidates.

Do not silently convert recommendation into decision or working language into immutable truth.

---

## 6. Structure for exploration vs structure for convergence

AI structure is useful in two different ways.

### Structure for exploration

Purpose:
create a **criticism surface**.

Properties:
- incomplete enough to challenge;
- assumptions visible;
- replaceable;
- explicitly provisional;
- optimized for discovering what is wrong or missing.

Examples:
- rough domain model;
- competing frames;
- tentative terminology;
- solution probe;
- provisional interaction taxonomy.

### Structure for convergence

Purpose:
stabilize a current baseline.

Properties:
- alternatives considered;
- evidence linked;
- important contradictions resolved or exposed;
- commitments explicit;
- suitable for downstream reliance.

The AI should not present exploratory structure with convergence-level certainty.

---

## 7. Problem–solution relationship

> **Separate commitment status, not problem and solution.**

Problem and solution may co-evolve.

The protocol rejects both:

- rigid "problem complete before solution";
- silent lock-in to the first plausible solution.

Working rule:

> **Commitment late; probes early and reversible.**

---

## 8. Solution Probe

A `PROBE` is a concrete concept used to learn.

It should state:

- learning question;
- assumptions exposed;
- expected learning;
- what would make us discard it.

After meaningful probe use:

1. What did we learn?
2. What assumption changed?
3. What does this imply about the problem/frame?
4. Did a new constraint emerge?
5. Is there an alternative interpretation?
6. Reopen, revise, discard or promote?

Do not default immediately to "improve the solution".

---

## 9. Shared conceptual language

Shared Language is a first-class cross-cutting concern, not a separate discovery phase.

For model-relevant concepts:

> **Preserve human source meaning, treat AI names as proposals, test meaning in use before stabilization, and keep language revisable.**

The AI should distinguish:

- source expression,
- interpretation,
- candidate naming,
- working agreement,
- canonical-for-now commitment.

See `04_SHARED_LANGUAGE_POLICY.md`.

---

## 10. Research behavior

Research may serve:

- landscape exploration;
- feasibility;
- decision support;
- verification;
- falsification.

Before non-trivial research, capture:

- question;
- why it matters now;
- current belief/hypothesis;
- what evidence could change the model or decision.

After research, produce an explicit **Model Delta**:

```text
REINFORCED / REFINED / CHALLENGED / NEW / NO CHANGE
```

Also capture:
- new uncertainty;
- changed decision;
- remaining hypothesis.

Research should change the model when warranted, not merely accumulate citations.

---

## 11. Analogy Boundary Check

When importing a prior framework, product or method:

1. What original problem did it solve?
2. What is similar?
3. What important assumptions differ?
4. What mechanisms transfer?
5. What must not transfer?

A useful analogy may still become a fixation source if its operating assumptions are silently imported.

---

## 12. Divergence rules

During deliberate divergence:

- avoid a single preferred high-completeness answer by default;
- preserve valuable independent human signal where relevant;
- prefer structurally distinct probes;
- use fragments/mechanisms before polished end states when useful;
- keep candidate language visibly tentative;
- expose competing models, not synonym lists;
- compare before ranking.

---

## 13. Convergence and commitment

Convergence is justified when:

- the current frame is stable enough for the decision horizon;
- important constraints are known;
- materially different directions were considered;
- critical assumptions were tested or explicitly accepted;
- high-impact terminology has enough shared meaning for current decisions;
- further exploration has diminishing expected information value;
- uncertainty remains visible.

A useful sequence:

`compare → expose uncertainty → challenge → decide → commit`

---

## 14. Discovery completion

Discovery is ready for handoff when:

- problem/opportunity frame is understandable;
- goals, scope and non-goals are explicit;
- consequential decisions are explainable;
- important shared concepts have sufficiently stable meanings for the handoff context;
- assumptions and evidence remain distinguishable;
- material external contracts are verified or deliberately deferred;
- remaining implementation questions are explicitly deferred;
- a new implementation context can proceed without reopening fundamental product decisions.

Readiness means:

> **stable enough + material unknowns explicit + downstream ownership clear**

—not "all questions answered".

---

## 15. Whole-baseline review before stable/public release

Before treating a protocol/discovery baseline as stable for public release:

- run independent adversarial review;
- search for contradictions;
- challenge unsupported certainty;
- inspect hidden assumptions;
- test handoff fitness;
- clean public citations and source claims;
- ensure public artifacts contain no private context.

Packaging is a decision, not merely formatting.
