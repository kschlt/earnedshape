# Interaction & State Model v0.2

> **Status:** experimental, protocol v0.2. Rules may still change between versions.

## 1. Orthogonal dimensions

Do not compress all interaction into one taxonomy.

### Discovery Mode — What is the dominant learning objective right now?
- `PROBLEM_EXPLORATION`
- `SOLUTION_EXPLORATION`
- `CONVERGENCE`

A mode is the dominant learning objective of the moment, not a phase (`01` §5). Expect many switches per session.

### Interaction Move — What cognitive move is useful?
- `ELICIT`
- `REFLECT`
- `RESEARCH`
- `DIVERGE`
- `CRITIQUE`
- `SYNTHESIZE`
- `COMPARE`
- `CLARIFY_MEANING`
- `CONVERGE`
- `DECIDE`
- `MAINTAIN`

### Human Contribution — What human cognition is valuable?
- `SITUATED_GROUNDING`
- `FRAMING_MEANING`
- `INDEPENDENT_POSITION`
- `JUDGMENT_EXCEPTIONS`
- `COMMITMENT_ACCOUNTABILITY`
- `NONE`

A binding may additionally model handoff tasks such as:
- `UNDERSTAND`
- `CONTRIBUTE`
- `VALIDATE`
- `DECIDE`

These are interaction tasks, not substitutes for the contribution model.

---

## 2. Core routing loop

```text
Read current discovery state
        ↓
What progress is useful now?
        ↓
What uncertainty / learning objective / decision dominates?
        ↓
Can AI resolve or maintain it without consuming valuable human cognition?
        ├─ yes → act, update state, continue
        └─ no
             ↓
What human contribution is valuable?
             ↓
Could AI output erase a useful independent human signal?
        ├─ yes → elicit / preserve signal first
        └─ no
             ↓
Is the uncertainty factual, semantic, normative, or evaluative?
             ↓
Research / clarify / contrast / challenge / decide
             ↓
Interpret contribution
             ↓
Update epistemic state + discovery objects + shared language
             ↓
Choose next move
```

---

## 3. Interaction principles

### 3.1 Elicit before generating — selectively

Use when human-origin information itself matters.

Examples:
- first frame;
- key criteria;
- high-impact trade-off;
- framing-bearing terminology;
- strong solution anchor.

Do not add friction to mechanical or easily verifiable work.

### 3.2 Ask for episodes, not only opinions

Use concrete situations to expose:
- actual workflow;
- exceptions;
- implicit constraints;
- terminology boundaries.

### 3.3 Question before recommending when meaning is unresolved

If the uncertainty is:
- what should matter,
- what a term means locally,
- which trade-off is acceptable,

more factual research may not solve it.

### 3.4 Research autonomously when uncertainty is externally resolvable

Do not make the human manually retrieve what AI can investigate.

### 3.5 Separate generation from critique

After creating a direction, explicitly test:
- counterexamples;
- opposite frames;
- contradicting evidence;
- failure conditions;
- hidden assumptions.

### 3.6 Separate exploration structure from convergence structure

When creating an exploratory model:
- label it provisional;
- expose assumptions;
- invite correction.

When producing a convergence artifact:
- show decision/evidence status;
- show unresolved uncertainty;
- identify what is now relied upon.

### 3.7 Shared-language intervention is selective

Trigger explicit terminology work only if:

> A different interpretation could change requirements, decisions, domain boundaries, responsibilities, priorities or handoff meaning.

Otherwise, keep moving.

---

## 4. Shared Language moves

Shared Language is not a separate mode.

Useful micro-moves include:

### `REFLECT_SOURCE`
Restate the human meaning without prematurely assigning a canonical name.

### `SEMANTIC_PROBE`
Ask a discriminating question:
- example,
- non-example,
- boundary,
- consequence.

### `OFFER_CANDIDATE_LANGUAGE`
Offer one or a few terms as proposals.

Prefer candidates with different conceptual implications over synonym lists.

### `ADOPT_WORKING_TERM`
Use a term for convenience without treating it as final.

### `TEST_IN_USE`
Apply the term to a concrete scenario.

### `REOPEN_TERM`
Rename, split, merge or deprecate when the model changes.

---

## 5. Turn economics

During active exploration, visible responses should optimize for the next contribution.

A compact default:

### What changed
Minimum state/model update.

### Why it matters
Consequence, ambiguity or contradiction.

### What is needed next
One high-value human contribution.

Long-form synthesis is justified for:
- complex understanding;
- candidate comparison;
- review;
- decision;
- stable artifact creation.

---

## 6. Working discovery state

Candidate semantic structure:

```yaml
discovery:
  protocol_version:
  mode:
  current_focus:
  current_learning_objective:

working_frame:
  actors:
  context:
  observed_situations:
  desired_outcomes:
  causal_mechanisms:
  constraints:
  competing_frames:

scope:
  in_scope:
  out_of_scope:
  deferred:

objects:
  probes:
  candidates:
  recommendations:
  decisions:
  commitments:

epistemic:
  evidence:
  human_inputs:
  inferences:
  assumptions:
  uncertainties:

concepts:
  - term:
    meaning:
    status: candidate | working | canonical_for_now | reopened | deprecated
    context:
    source_expression:
    provenance:
    example_boundary:
    open_issue:
    rename_history:

evaluation:
  high_impact_decisions:
  unresolved_high_risk_assumptions:
  readiness_gaps:

learning:
  protocol_hypotheses_under_test:
  observed_process_failures:
  research_model_deltas:
```

This is a semantic candidate, not a fixed serialization contract.

---

## 7. Three distinct status dimensions

Do not confuse them. The decision/commitment and shared-language dimensions are the state encoding of the Progressive Commitment ladder (`01` §3), not a separate mechanism.

### Epistemic status
- Evidence
- Human Input
- Inference
- Assumption
- Uncertainty

### Decision / commitment status
- Probe
- Candidate
- Recommendation
- Decision
- Commitment
- Deferred

### Shared-language status
- Candidate
- Working
- Canonical-for-now
- Reopened
- Deprecated

A term can be `canonical-for-now` while a claim using that term remains an `assumption`.

A solution can be a `probe` while some facts inside it are well-supported `evidence`.

---

## 8. State update rules

State maintenance should be:

- continuous;
- mostly invisible;
- reversible;
- traceable;
- cheap;
- selective.

The human should not approve routine state maintenance.

Lifecycle:

```text
working state
→ working state
→ working state
→ review candidate
→ stable snapshot
```

Artifacts are projections of state, not the primary memory mechanism.

---

## 9. Research Model Delta

After focused research, record:

```yaml
research_delta:
  question:
  previous_model:
  result: reinforced | refined | challenged | new | no_change
  changed_items:
  new_uncertainty:
  decision_impact:
  remaining_hypothesis:
```

The purpose is to make the epistemic effect of research visible.

---

## 10. Analogy record

For influential external precedents:

```yaml
analogy:
  source:
  original_problem:
  similarities:
  important_differences:
  transferable_mechanisms:
  non_transferable_assumptions:
```

This is especially useful when a mature prior model risks defining the new problem by analogy.

---

## 11. State integrity requirements

A binding should make it difficult to:

- lose explicit commitments;
- present inference as evidence;
- leave superseded assumptions active;
- forget deferred decisions;
- maintain contradictory constraints silently;
- promote a probe into commitment without an explicit transition;
- treat repeated terminology as proof of shared meaning;
- preserve a polished term while its actual meaning has drifted;
- create a handoff whose key decisions or concepts cannot be reconstructed.
