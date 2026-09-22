# CP-09 — Analogy Records for the Protocol's Own Imports

> **Published record of change proposal CP-09** (see [`docs/review/disposition.md`](../docs/review/disposition.md)). The protocol requires an analogy boundary check for imported frameworks; this file applies it to the protocol's own four imports. `source-research/03` is one of the unpublished research reports described in [`docs/provenance.md`](../docs/provenance.md). The fixes it proposes are not yet applied to `protocol/`.

> **Status:** Proposal artifact. Candidate appendix to `protocol/`, not applied there.
> **Executes:** change proposal CP-09, addressing finding F-18 — the protocol mandates an Analogy Boundary Check (`01_PROTOCOL_V0.2` §11, schema in `02_INTERACTION_AND_STATE_MODEL` §10) and has never performed one on its own four imports.
> **Also:** the cheapest available exercise of `CAP-15`, on material already at hand.

A check that finds nothing is theatre. §5 states what these four found.

---

## A-01 · Domain-Driven Design / Ubiquitous Language

```yaml
source: Domain-Driven Design; Ubiquitous Language; Bounded Context
original_problem: >
  Keeping a team of developers and domain experts aligned on one model,
  over years, in a codebase, where the model IS the code.
similarities:
  - language and model co-evolve; a rename signals a model change
  - "canonical" is bounded by context, not global
  - forced lexical uniformity across contexts is a mistake
important_differences:
  - DDD aligns a multi-party team with shared incentives and persistent memory;
    this protocol governs a two-party dyad where one party has neither
  - in DDD the compiler is a witness: a term used wrongly breaks something.
    In a conversation nothing witnesses misuse
  - DDD's contexts are organisational and architectural; a discovery's
    "context" is a conversational scope with no enforcement surface
  - DDD assumes the model will be built; discovery may end in a decision not to
transferable_mechanisms:
  - language/model co-evolution
  - context boundaries instead of forced uniformity
  - rename, split and merge as evidence of an improved model
non_transferable_assumptions:
  - that repeated use demonstrates shared meaning — in DDD it is checked by code
  - that a glossary is maintained by parties with a shared stake in its accuracy
  - that "ubiquitous" is achievable, or desirable, inside an exploratory dialogue
```

**Defect surfaced:** DDD and Ubiquitous Language appear **nowhere** in `protocol/` or `research/`, although `04_SHARED_LANGUAGE_POLICY` §§7–9 rest on them. The import is invisible above `source-research/04`. An unnamed import cannot be boundary-checked by a reader, which is how it stayed unchecked.

---

## A-02 · Common ground, lexical entrainment, conceptual pacts

```yaml
source: psycholinguistics of dialogue — common ground, lexical entrainment, conceptual pacts
original_problem: >
  Explaining how two humans establish reference in dialogue, largely in
  referential communication tasks with concrete referents, over minutes.
similarities:
  - a pact is partner-specific, local and revisable
  - shared words do not entail shared concepts
important_differences:
  - the studied process is symmetric between peers; a human and an LLM adapt
    asymmetrically, and mostly in one direction — toward the model's register
  - both human partners have persistent memory and a stake in being understood;
    the model has neither and cannot hold a pact across sessions
  - the referents are concrete and jointly visible; product concepts are neither
  - the timescale is minutes, not weeks
transferable_mechanisms:
  - lexical agreement is not conceptual agreement
  - pacts are local and revisable rather than definitional
non_transferable_assumptions:
  - that entrainment implies mutual adaptation
  - that a pact, once established, persists in both parties
  - that the effect sizes observed on concrete referents transfer to abstract
    model-bearing terminology
```

**Consequence:** the asymmetry cuts both ways. It strengthens the candidate-first rule — the human drifts toward the model's language more than the reverse. It also weakens the transfer of the entrainment evidence itself, which `research/02` leans on more heavily than the difference in symmetry supports.

---

## A-03 · Turn (prior work: adaptive cognitive handoff)

```yaml
source: Turn — adaptive cognitive handoff for predominantly autonomous implementation agents
original_problem: >
  Placing human intervention well in work that an agent otherwise executes
  alone, where the goal is throughput at acceptable quality.
similarities:
  - initiative as a property of the move, not a role
  - handoff as a first-class object
  - human attention treated as a scarce resource
important_differences:
  - in implementation the human's involvement is overhead to be minimised;
    in discovery the human's cognition IS the product
  - implementation work is externally verifiable — tests, builds, runtime;
    discovery has no such witness
  - Turn's success measure is throughput with maintained quality; discovery's
    is understanding, breadth before commitment, and a handoff that holds
transferable_mechanisms:
  - dynamic initiative
  - the handoff artifact
  - explicit decision rights per move
non_transferable_assumptions:
  - that human involvement is a cost to be reduced
  - that the work object can be verified without the human
  - that increasing autonomy is the direction of improvement
```

**Defect surfaced — the important one.** `D-04 "Human attention is scarce"` is a Turn-derived premise. In Turn's setting, minimising human involvement is the goal. In discovery, minimising human involvement is a **failure mode** — it is the thing the protocol's own governing principle exists to prevent. The protocol currently holds both: attention scarcity as a design driver, and "preserve the cognition that materially improves quality" as the objective. They are not identical, and where they conflict — an expensive elicitation that the human would rather skip — the protocol does not say which wins. Evidence Case 02 recorded that Turn was over-assimilated once (E-02-07); this is a second instance, and it survived into v0.2 unexamined.

---

## A-04 · Cognitive forcing functions

```yaml
source: cognitive forcing functions in AI-assisted decision-making
original_problem: >
  Reducing overreliance on AI advice in single discrete decisions that have a
  ground truth, in short sessions with non-expert users.
similarities:
  - deliberate friction improves appropriate reliance
  - explanations and confidence scores alone do not
important_differences:
  - those tasks have an accuracy criterion; a discovery decision has none
    available at the time it is made
  - the decision is one moment; a discovery commitment is distributed over weeks
  - the studies separate decider from evaluator; here they are the same person
  - the effective designs were rated worse by users — and a solo practitioner
    can simply switch them off
transferable_mechanisms:
  - friction proportional to consequence
  - explanation is not calibration
non_transferable_assumptions:
  - that overreliance is detectable in the moment
  - that a fixed forcing schedule is appropriate to open-ended work
  - that an external accuracy criterion exists against which reliance is judged
```

**Consequence:** the missing ground truth is why `Beneficial AI Uptake / Defective AI Resistance` — recommended by `source-research/03` and dropped from `protocol/05` §3 — is not implementable as specified. Finding F-13 flagged that drop as undocumented. It now looks **justified but unrecorded**: the right fix is a note saying why, not reinstating the metric. Seeded defective cases would be the only way to measure it, and that is a controlled-study instrument, not a run-level signal.

---

## 5. What this exercise found

Four checks, four findings, none of them cosmetic:

1. **An invisible import.** DDD/Ubiquitous Language carries `04_SHARED_LANGUAGE_POLICY` and is named nowhere above the raw research. *Proposed fix:* name it in `04` §1 and link the record.
2. **An unexamined inherited premise.** `D-04` imports attention scarcity from a setting whose goal is the inverse of this protocol's. *Proposed fix:* state the conflict in `03_DECISION_RIGHTS` §8 and say which side wins when they collide.
3. **An over-leveraged evidence family.** The entrainment work is asymmetric to the human–LLM case in a way `research/02` does not qualify. *Proposed fix:* one qualifying sentence; the practical rule it supports is unaffected.
4. **A justified-but-unrecorded omission.** The defective-AI-resistance metric was dropped for a good reason that nobody wrote down. *Proposed fix:* record the reason in `protocol/05` §3.

Two of these — 2 and 4 — are things no reader could have reconstructed from the pack. That is the argument for the mechanism: the check is cheap, and it found an inherited premise pulling against the protocol's own governing principle.

## 6. Where this should live

As `protocol/appendix-analogy-records.md`, referenced from `01_PROTOCOL_V0.2` §11, so that the rule and the project's own compliance with it sit next to each other. A protocol that mandates a check and cannot show its own is not credible on the point.
