# Capability Catalogue

> **Owns:** the capabilities derived from the protocol, what each requires, what each must emit, and how each is evaluated on both levels.
> **Status:** Draft. The Core/Extended split is the proposal from change proposal CP-11 and is not yet an accepted protocol decision.
> **References:** change proposals (`CP-nn`) and their current status are in [`docs/review/disposition.md`](../docs/review/disposition.md); review findings (`F-nn`) in [`docs/review/`](../docs/review/2026-09-adversarial-review-v0.2.md); the Case 01 and Case 02 codes point into unpublished retrospectives and are explained in [`docs/provenance.md`](../docs/provenance.md). Phase 1 is described in [`docs/phase-1-feasibility.md`](../docs/phase-1-feasibility.md).
> **Vendor-free by construction:** no entry names a harness, a hook, a skill or a file format. `initial_form` is `?` everywhere until the Phase 1 spikes report what is reachable.

## How to read an entry

- **class** — `observation` records without changing what anyone does; `enforcement` changes behaviour. The distinction decides what a baseline run may contain: all observation on, all enforcement off.
- **must emit** — the events without which this capability cannot be evaluated at all. If the surface cannot emit them, the capability may still be *useful* there, but its effect there is not measurable, and that must be said out loud rather than assumed away.
- **eval L1** — enforcement fidelity: did it fire when it should, and not when it shouldn't. A failure is a build problem.
- **eval L2** — method value: did it produce the promised benefit. A failure is a protocol problem, and no better building fixes it.
- **falsified by** — what an honest negative result would look like. An entry without one is not a hypothesis, it is a preference.

---

## Core

### CAP-01 · Persistent discovery state
**class** enforcement · **depends on** —
**derives from** protocol D-10, `02_INTERACTION_AND_STATE_MODEL` §6, §8
**required** Discovery objects, epistemic entries, deferred questions and concepts survive the session boundary and are readable at the start of the next session without the practitioner restating them.
**must emit** `run.started`, `object.created`, `object.status_changed`
**eval L1** After a session boundary, is the state that existed at close present at open, without loss? Measured by replaying the event stream against the state and diffing.
**eval L2** Fewer re-decisions of already-settled questions; less rediscovery in handoff; the practitioner does not re-explain context.
**falsified by** State is maintained faithfully and nothing downstream improves — handoffs are no better, rediscovery is unchanged, and the maintenance cost is real.
**rollback** Stop writing; the state remains readable as a file. No migration.

### CAP-02 · Run observation
**class** observation · **depends on** —
**derives from** `05_EVALUATION_AND_LEARNING` §11; doc 10 §9
**required** An enrolled run produces a run record and an append-only event stream at a declared fidelity. Unenrolled sessions produce nothing.
**must emit** the full required set in `02-event-vocabulary.md`
**eval L1** `seq` gaps; events reconstructable against an independently kept manual log for one calibration run.
**eval L2** Not applicable — this capability is the instrument, not a treatment. Its value question is whether the recorded data can actually answer a protocol question, and that is answered by the first analysis attempt, not by a metric.
**falsified by** The stream is complete and no hypothesis becomes decidable from it.
**rollback** Stop observing. Nothing else depends on it functionally — by design, since a product may not require being observed.

### CAP-03 · Explicit object status transitions
**class** enforcement · **depends on** CAP-01
**derives from** protocol §3 Progressive Commitment, D-08, D-17
**required** An object's status changes only through a recorded transition carrying a rationale. Repeated use, fluency or elapsed time never promote an object.
**must emit** `object.status_changed`
**eval L1** Rate of objects whose status changed with no transition event; rate of transitions with an empty rationale.
**eval L2** Fewer objects arriving at commitment without a traceable path; the practitioner can name what an object's status was at a past decision point.
**falsified by** Transitions are recorded faithfully and commitment quality is unchanged, while the recording cost is visible in turn count or interruption.
**rollback** Downgrade to status-as-label without transitions.

### CAP-04 · Recorded commitment act
**class** enforcement · **depends on** CAP-01, CAP-03
**derives from** protocol §4.5, D-08; change proposal CP-06
**required** A commitment exists **only** as a recorded transition carrying object, owner, date, rejected alternative, rationale, supporting evidence references and revisit condition. No other route creates a commitment.
**must emit** `commitment.recorded`
**eval L1** Commitments present in the final baseline with no corresponding event; events with a missing rejected alternative or revisit condition.
**eval L2** Decision explainability without the original AI; fewer no-new-evidence reopenings; the receiving context can reconstruct why.
**falsified by** Complete commitment records and no improvement in explainability or reopening rate.
**rollback** Remove the requirement; existing records stay valid.

### CAP-05 · Deferred decision register
**class** enforcement · **depends on** CAP-01
**derives from** protocol §14, the deferred-decision register (`07_DECISIONS_AND_OPEN_QUESTIONS` §B up to v0.2, now [`docs/technical-decisions.md`](../docs/technical-decisions.md))
**required** A deliberately deferred question is recorded with its reason and the point at which it should be decided, and remains retrievable until resolved.
**must emit** `deferral.recorded`, `deferral.resolved`
**eval L1** Deferrals visible in the transcript but absent from the register; resolved questions never closed.
**eval L2** Fewer deferred questions rediscovered as surprises downstream; readiness judgements that hold.
**falsified by** The register is complete and downstream surprises occur at the same rate.
**rollback** Keep the list, drop the discipline.

### CAP-06 · Recorded challenge
**class** enforcement · **depends on** CAP-01
**derives from** change proposal CP-05; Case 01 AP-02 "Friendly AI Consensus"
**required** A substantive challenge to a high-impact object — from the AI, the human, or an external reviewer — is recorded with its resolution, and an unresolved challenge is visible at handoff.
**must emit** `challenge.raised`, `challenge.resolved`
**eval L1** Challenges visible in the transcript but unrecorded; challenges recorded but never resolved and never surfaced at handoff.
**eval L2** Whether recorded dissent later proves to have been right — i.e. whether overruled challenges predict reopenings. This is the one capability with a genuinely predictive test available at n=1.
**falsified by** Challenges are recorded and their resolution has no relationship to anything that happens later.
**rollback** Stop recording; the AI may still challenge in conversation.

### CAP-07 · Epistemic status separation
**class** enforcement · **depends on** CAP-01
**derives from** protocol §4.1, `02_INTERACTION_AND_STATE_MODEL` §7
**required** Evidence, human input, inference, assumption and uncertainty remain distinguishable in state, independently of an object's decision status.
**must emit** `epistemic.recorded`, `epistemic.status_changed`
**eval L1** Claims in state with no epistemic status; inferences presented as evidence in a produced artifact.
**eval L2** Fewer commitments resting on unmarked assumptions; assumption-driven rework identified earlier.
**falsified by** The separation is maintained and no downstream decision changes because of it.
**rollback** Collapse to a single "known" bucket.

### CAP-09 · Handoff artifact and cold-start test
**class** enforcement · **depends on** CAP-01, CAP-04, CAP-05
**derives from** protocol §14; `05_EVALUATION_AND_LEARNING` §3
**required** A run ends with an artifact from which a context that was not present can proceed, and that claim is **tested** by such a context rather than asserted.
**must emit** `handoff.produced`, `coldstart.tested`
**eval L1** Runs ending without a handoff artifact; handoffs never cold-start tested.
**eval L2** Cold-start blockers by severity — the pack's own primary outcome measure.
**falsified by** Handoffs are produced and tested and the blocker count does not fall as the protocol matures.
**rollback** Produce the artifact, drop the test. (The test is the expensive half and the informative half.)

### CAP-10 · Adversarial challenge before convergence
**class** enforcement · **depends on** CAP-06
**derives from** change proposal CP-01; Case 01 Phase 9, G6, L4, M-03; Case 02 E-02-20
**required** Before a high-impact commitment, the current model has survived one deliberate attempt to break it, by a party or context independent of the pair that built it. Findings are recorded as challenges; a narrow verification pass confirms the named blockers are closed.
**must emit** `adversarial_review.completed`, plus `challenge.raised` per finding
**eval L1** Commitments made with no preceding review event; reviews with no recorded findings (a review that finds nothing is usually a review that did not happen).
**eval L2** Whether findings are material — do they change the model, or only polish it? Case 01's own evidence predicts precision rather than redesign, which is a testable prediction.
**falsified by** Reviews consistently produce only cosmetic findings, or produce material findings that would have surfaced anyway.
**rollback** Demote to a recommended practice.

---

## Extended

### CAP-08 · Contradiction surfacing
**class** enforcement · **depends on** CAP-01, CAP-07
**required** Two active constraints or claims that cannot both hold are surfaced rather than held silently.
**must emit** `challenge.raised` with `by: system`
**eval L1** Known contradictions present in state and never surfaced (measurable only with seeded cases).
**eval L2** Contradictions caught before commitment rather than at handoff.
**falsified by** Detection works and the contradictions found are all trivial.

### CAP-11 · Concept entry for model-relevant language
**class** enforcement · **depends on** CAP-01
**derives from** `04_SHARED_LANGUAGE_POLICY`; D-14, D-15
**required** A term whose different interpretation would change requirements, decisions, boundaries or handoff meaning gets an entry with status, meaning, context and — where useful — the human source expression.
**must emit** `concept.introduced`, `concept.status_changed`, `concept.tested_in_use`
**eval L1** Model-bearing terms in use with no entry; entries whose status never changes across a run where the model clearly did.
**eval L2** Late renames that change downstream decisions; whether the human can define a canonical term without copying AI wording.
**falsified by** Entries are maintained and late semantic corrections occur at the same rate — with the terminology overhead visible.
**note** The selection trigger is subjective and evaluated by the AI. Expect both over- and under-application, and record which.

### CAP-12 · Research model delta
**class** enforcement · **depends on** CAP-01, CAP-07
**derives from** protocol §10, D-20
**required** Focused research ends with a recorded delta: what changed, what became more uncertain, which decision became possible.
**must emit** `research.delta_recorded`
**eval L1** Research episodes with no delta recorded.
**eval L2** Proportion of research that changes the model rather than accumulating citations.
**falsified by** Deltas are recorded and are almost always `no_change` — which would mean the research questions, not the recording, are the problem.

### CAP-13 · Solution probe and debrief
**class** enforcement · **depends on** CAP-01, CAP-03
**derives from** protocol §8, D-09
**required** A concrete solution used to learn is labelled a probe and debriefed: what was learned, which assumption changed, what it implies for the frame, and its disposition.
**must emit** `probe.debriefed`
**eval L1** Objects functioning as probes without the label; probes never debriefed.
**eval L2** Whether probe learning reaches the problem frame — measurable as frame changes traceable to a debrief.
**falsified by** Debriefs happen and the frame never changes as a result, i.e. backpropagation was already happening informally.

### CAP-14 · Independent human position at anchor-risk events
**class** enforcement · **depends on** —
**derives from** protocol §4.3; change proposal CP-03
**required** At an enumerated anchor-risk event — first framing of a newly opened object, selection among materially different directions, naming of a framing-bearing concept, statement of a high-impact criterion, a decision the human will later defend alone — a brief independent human position is captured before strong AI output.
**must emit** `human_position.elicited` with `before_ai_output`
**eval L1** Anchor-risk events passing with no elicitation — computable only because the trigger is an enumerated list rather than a judgement call.
**eval L2** Whether the human's independent position differs from what they later endorse, and whether preserved differences prove useful.
**falsified by** Positions are elicited and never differ materially from the AI's subsequent framing — or differ and are always abandoned for good reason.
**note** This is the capability most likely to be experienced as friction. Record the cost.

### CAP-15 · Analogy boundary record
**class** enforcement · **depends on** CAP-01
**derives from** protocol §11, D-19
**required** When a prior framework, product or method is imported as precedent, a record states the original problem, what transfers, and what must explicitly not transfer.
**must emit** `analogy.recorded`
**eval L1** Influential precedents used with no record.
**eval L2** Whether a recorded non-transferable assumption is later caught being imported anyway.
**falsified by** Records are produced and no import error is ever caught by one.
**note** The protocol does not currently apply this to its own imports (finding F-18). The capability should be exercised on those four first — the cheapest possible test, on material already at hand. Done by hand as change proposal CP-09: [`research/analogy-records.md`](../research/analogy-records.md) — each of the four records produced a finding, none of them cosmetic.

---

## Reserved

An identifier is allocated the moment a proposal depends on it, so that it cannot be reused while the proposal is open. A reservation is not a specification.

### CAP-16 · Information-loss gate
**status** reserved, not specified · **class** enforcement · **from** change proposal CP-18
Before an irreversible normalization, record what source-grounded information is being discarded and what reconstructing it would cost. v0.2 has this only for terminology; Case 01 identified the general form as transferable to any system that ingests and transforms external information.
**would emit** `normalization.recorded {discarded, reconstruction_cost}`

---

## What is deliberately absent

- **Adaptive routing / the five-factor router.** Untested as a router, and there is no event that would show it fired. Adding a capability for it now would manufacture the appearance of a mechanism.
- **Mode tracking.** The mode taxonomy is under an open change proposal (CP-02); building a capability on a taxonomy that may be renamed is premature.
- **Turn economics.** Depends entirely on whether `turn.recorded` is reachable. Phase 1 decides whether this is a capability or a demoted hypothesis.
