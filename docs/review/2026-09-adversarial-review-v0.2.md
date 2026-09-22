# Orientation & Adversarial Review — Discovery Pack v0.2

> **Published record.** This is the review as written on 10 September 2026 against *Discovery Pack v0.2*, the private working package from which this repository was later derived. It is reproduced unchanged apart from this note, because the point of publishing it is that the findings and change proposals can be checked against what was done with them — see [`disposition.md`](disposition.md).
> File names such as `08_HANDOVER`, `README.md`, `evidence/` or `source-research/` refer to that package, not to this repository. What each of them is, and what the ID schemes (`F-nn`, `CP-nn`, `D-nn`, Case 01/02 codes) mean, is explained in [`docs/provenance.md`](../provenance.md).

> **Status:** Non-normative review input. Project layer: same as `08_HANDOVER_TO_NEXT_AGENT.md` (project input, not protocol, not evidence, not research).
> **Scope:** Task 1 of the handover only — orientation and whole-baseline adversarial review.
> **Protocol changes made:** none. Every proposed change is stated as an explicit change proposal in §5.
> **Reviewer independence:** partial. This review is by an AI agent, on a baseline produced by an AI–human pair. It is *not* the independent adversarial review that D-21 / §15 requires. See Q6.

---

## 1. What this project is trying to become

My reading, stated so it can be corrected:

**The asset is a versioned, technology-independent protocol for one human and one AI doing pre-implementation discovery together, plus an evidence apparatus that lets the protocol be revised on something better than taste.**

Three things follow from that, and they are what make the project unusual:

1. **The protocol is not a prompt and not a workflow.** It is a set of semantics — what kinds of objects exist (probes, candidates, decisions, commitments, concepts, assumptions), what status they carry, who may change that status, and what the AI may do without asking. A prompt is a binding-level artifact; the protocol is what a prompt would have to realize.

2. **The optimization target is inverted relative to normal AI tooling.** Most AI assistance optimizes for the completeness of the AI's answer. This protocol optimizes for *the next high-value human contribution*, and treats a fluent, complete AI answer as a potential loss event (anchoring, agency erosion, silent commitment). The core thesis in `README.md` is a claim about what to *protect*, not about what to automate.

3. **Method evolution is part of the product.** The evidence layering (`evidence/` ≠ `research/` ≠ `protocol/` ≠ `source-research/`), the changelog, the "what this does not prove" sections and the learning backlogs mean the intended end state is not "a good protocol" but "a protocol that accumulates evidence about itself".

The intended long-run shape, as far as I can infer it: a public protocol spec with independent version history, one or more reference bindings (Claude Code as first candidate), an evidence archive of instrumented discovery cases, and an evaluation harness that can tell whether a protocol change actually improved anything.

**What it is trying *not* to become**, also inferred: a multi-agent discovery platform, a methodology brand, a portfolio piece, or a glossary/process bureaucracy. The pack states all four resistances explicitly, which is a good sign.

**The biggest structural risk to that ambition** is stated in the pack's own words (`README.md`, "Current maturity") and I agree with it: *the next phase should make these mechanisms testable, not merely more elaborate*. v0.2 is currently far more elaborate than it is testable. Almost everything in §2.5 below is a mechanism with a name, a rationale and no instrument.

---

## 2. Layer separation

The handover asks for five categories. I found that two of them (invariants and evidence-backed claims) only separate cleanly if a third distinction is added: *what is invariant because it is well-supported* vs *what is invariant because it was decided*. I have marked that below.

### 2.1 Protocol invariants (change only via explicit revision)

These are the load-bearing commitments. I would not touch any of them on current evidence.

| Invariant | Source | Why it holds |
|---|---|---|
| The asset is a versioned protocol, separate from any binding | D-01, D-02 | Design decision; supported by the observation that harness limits would otherwise rewrite semantics |
| Five human contributions: Situated Grounding, Framing & Meaning, Independent Position/Authorship, Judgment & Exceptions, Commitment & Accountability | D-05 | Framed as *epistemic/normative roles*, not capability claims — that framing is what makes them defensible |
| Human testimony is evidence, not ground truth | `01_PROTOCOL` §4.1 | Directly supported by RE elicitation research (requirements are co-constructed) |
| Progressive Commitment: proposal ≠ working model ≠ recommendation ≠ decision ≠ commitment | D-08, D-17 | The central mechanism; everything else is instrumentation for it |
| `Probe ≠ Candidate ≠ Recommendation ≠ Decision ≠ Commitment` | D-09 | Same |
| Problem and solution co-evolve; separate *commitment status*, not problem and solution | D-07, §7 | Well supported (Dorst & Cross; RE) |
| Initiative is a property of the move, not a role | D-06 | Mixed-initiative HCI; observed in both cases |
| AI must not silently commit on the human's behalf | §4.5, `03` §7 | Design decision, high confidence |
| Shared Language is first-class and cross-cutting, **not** a sixth contribution | D-14 | Decision + research support |
| `Meaning before commitment`, not meaning before naming | D-16 | Research *changed* this from v0.1 — an actual falsification event, worth preserving |
| AI names for model-relevant concepts start as proposals | D-15 | Supported as risk-justification, not as measured effect |
| "Canonical" means canonical-for-now-and-context | §7 of `04` | DDD + conceptual pacts |
| No single protocol score; quality + agency gates | D-11, D-12 | Well supported by evaluation research |
| Public artifacts are durable; evidence hygiene precedes publication | D-13 | Decision |

### 2.2 Experimental hypotheses (named, unproven, must not be presented as practice)

The pack is honest about these, and the honesty is correctly located (handover §4, `01_EVIDENCE` §7, `04` §15, Case 02 HYP-01..05). Consolidated:

- five-factor adaptive routing as an actual router;
- the exact Independent-Position / human-first trigger;
- explicit `PROBE` labelling and a mandatory probe debrief;
- the shared-language lifecycle `candidate → working → canonical-for-now → reopened`;
- visible Human/AI/External provenance labels;
- a scenario gate before canonicalization;
- persistent external state beating strong implicit memory;
- concept registry vs implicit memory;
- the proposed run-level metrics as predictors of downstream implementation quality;
- exploration-turn brevity;
- bounded-uncertainty readiness;
- the analogy boundary check as a *mechanism* (its diagnosis is evidenced; its ritual is not).

**Naming problem:** these hypotheses exist in five overlapping ID spaces — `H-01..H-12` (Case 02 §15), `H-SL-01` (addendum), `E1..E10` (`05` §10), `P-01..P-14` / `E-01..E-08` / `T-01..T-10` (`07`), and `M-01..M-12` (Case 01). They partly duplicate each other. See CP-11.

### 2.3 Evidence-backed claims (external research, not this project's own cases)

Strong enough to rely on:

- Human+AI is not automatically synergistic; average synergy vs the better single actor was negative (Vaccaro et al. 2024, 106 experiments). This is the strongest single result in the pack and it justifies the whole "design the coupling" premise.
- Generative AI can increase individual output quality while homogenizing outputs (Doshi & Hauser; de Rooij & Biskjaer meta-analysis).
- AI examples can increase design fixation and reduce divergent output (Wadinambiarachchi et al., CHI 2024).
- LLM use *before* independent ideation reduces ownership and self-efficacy; use *after* is better (CHI 2025 experiment).
- Explanations and confidence scores are not robust moderators of appropriate reliance; cognitive forcing works better but is disliked.
- Requirements are co-constructed, not extracted (Ferrari et al.; only 30–38% traceable to original customer ideas).
- Problem/solution co-evolution (Dorst & Cross).
- Lexical entrainment and human→computer lexical alignment are real; shared language reduces referential cost; conceptual pacts are local and revisable.
- Structured scaffolding can beat generic chat (Supermind Ideator) — but see F-10.

**Missing from the curated layer, and it matters:** Shin et al. (CHI 2025, N=280) found *no improvement in problem-frame quality* from LLM support, a widened expert/novice gap, and lower perceived agency among novices. This is the study closest to the project's actual target task, and it is the strongest disconfirming evidence in the whole pack. It appears once, in `source-research/04`, and never reaches `research/` or `protocol/`. See F-10 / CP-07.

### 2.4 Process evidence (this project's own cases — weaker, and dependent)

- **Case 01 (Cookframe, object-level):** intermediate models as criticism surfaces; human held product/scope decisions; hypothesis-led research beat broad research; external adversarial review at the right moment, then a narrow verification review, then stop; source/canonical/derived separation; explicit deferral.
- **Case 02 (meta-level):** the same criticism-surface pattern; human framing/boundary correction as the highest-value human act; research produced material model change; analogy over-assimilation (Turn); deferral preserved openness; no whole-package adversarial review happened.
- **Case 02A (post-hoc):** rapid uptake of AI/research-originated terminology is observable; causal anchoring is **not** established. The addendum's refusal to retro-fit the evidence is the single most disciplined move in the pack.

Correct epistemic label, already stated by the pack: **cross-level dependent recurrence, not replication.**

### 2.5 Implementation requirements (things any binding must provide)

Extracted from `02` §11 and the invariants — these are genuinely normative for a binding:

1. Persist explicit commitments across sessions; losing one is a defect.
2. Keep epistemic status (evidence / human input / inference / assumption / uncertainty) distinguishable from decision status.
3. Make status transitions explicit and traceable — in particular, no probe→commitment promotion without a recorded transition.
4. Keep deferred decisions retrievable and reviewable.
5. Surface contradictory active constraints rather than holding both silently.
6. Support reopening/renaming/splitting concepts with rename history where meaningful.
7. Make state maintenance cheap, continuous and *not* human-approved.
8. Produce a handoff from which key decisions and concepts can be reconstructed by a party who was not present (cold-start).
9. Keep protocol semantics separable from harness mechanics (no harness limit silently redefining a rule).

**Gap:** none of these define *what a commitment physically is* — who writes it, in what form, with what fields, and how it is revoked. That is the smallest missing piece blocking any binding. See F-22 / CP-06.

### 2.6 Still-open implementation choices (correctly deferred)

`T-01..T-10` are the right list: name, repo topology, first harness, state serialization, skill/hook/agent architecture, review/handoff surface, evaluator architecture, release workflow, concept storage, provenance visibility.

I would add three that the pack does not list:

- **T-11 — Conformance definition.** What makes a run "v0.2-conformant"? Without this, Case 03 cannot claim to test the protocol; it can only claim to be inspired by it.
- **T-12 — Trace/telemetry format.** `05` assumes traces exist. Nothing defines an event.
- **T-13 — Session/context boundary handling.** State exists because context is lost; nothing says what happens at a session boundary, at context limit, or when the model version changes mid-project.

---

## 3. Adversarial review of Protocol v0.2

Severity: **H** = fix before Case 03; **M** = fix before public release; **L** = hygiene.

### 3.1 Contradictions and internal tension

**F-01 (M) — The mode taxonomy separates exactly what §7 forbids separating.**
`01` §7 says "separate commitment status, not problem and solution", yet §5 names the two exploration modes `PROBLEM_EXPLORATION` and `SOLUTION_EXPLORATION` and `02` §1 makes Discovery Mode the answer to "Where are we?". A reader implementing the protocol will build a phase machine out of the mode names and reintroduce the very sequencing the protocol rejects. `P-01`/`P-06` acknowledge the taxonomy is open, but the protocol still uses it normatively.

**F-02 (H) — Adversarial challenge is a release ritual, not a convergence gate.**
§15 places independent adversarial review before *public release*. But the best-evidenced convergence mechanism in the entire pack is Case 01's `broad adversarial review → fixes → narrow verification review → stop` (Case 01 Phase 9, G6, L4, M-03, and lesson L5), and Case 02's single most-cited defect (E-02-20) is that this did not happen. §13's justification list for convergence contains seven conditions and *not one of them is "the model survived a deliberate attempt to break it"*. (Precision, added after review: §13's closing sequence does read `compare → expose uncertainty → challenge → decide → commit`, so challenge is not absent from the section — but it appears as a step in a suggested order, not as a condition that justifies convergence, and nothing requires the challenge to come from a party independent of the pair that built the model.) The protocol learned this lesson only as a packaging step. This is the largest substantive gap I found.

**F-03 (H) — The Independent-Position trigger is undecidable and is assigned to the conflicted party.**
§4.3: "The trigger is whether a strong AI anchor would destroy information worth observing." The AI must evaluate, before producing output, whether its own output would erase a human signal it has not yet seen. That is not evaluable in principle, and the evaluator is the party whose output is the risk. `02` §3.1 gives examples, which helps, but the normative rule remains a self-judgment. This also makes hypothesis E2 untestable as written: you cannot measure compliance with an unobservable trigger.

**F-04 (M) — Anti-bureaucracy rule vs. the concept record.**
`04` §11 and `02` §6 specify a concept entry with nine fields plus rename history and a five-state lifecycle; `03` §10 and `04` §14 list "vocabulary bureaucracy" as a failure mode; `04` §3 gates entry on a subjective question the AI answers alone. The protocol therefore both mandates the machinery and warns against using it, with no operational threshold. Under-application and over-application are equally consistent with the text.

**F-05 (L/M) — Concept status is not context-scoped, but canonicity is.**
`04` §9 says a term may legitimately be canonical in Billing and different in Identity. The state schema attaches one `status` and one `context` to one `term`. A term that is canonical-for-now in one context and candidate in another cannot be represented without duplicating the entry, and nothing says duplication is intended.

**F-06 (M) — "Artifacts are projections of state" is asserted by a baseline that is entirely artifacts and has no state.**
D-10 flags the runtime effect as experimental, which is honest, but `02` §8 states the lifecycle as normative. Meanwhile `02` §8 wants maintenance "mostly invisible" and un-approved, while `02` §11 requires explicit, traceable transitions. Invisible-but-traceable is achievable, but only if the protocol says which mutations are silent and which are events. It does not.

### 3.2 Redundancy and unnecessary complexity

**F-07 (M) — Four devices encode one idea.**
Progressive Commitment (`01` §3), structure-for-exploration vs structure-for-convergence (`01` §6), three status dimensions (`02` §7), and half the failure-pattern lists (`03` §10, `04` §14) are all instruments for *"do not let tentative become committed by fluency and repetition"*. The four are not wrong, but they are not orthogonal, and each carries its own vocabulary. A single commitment ladder with typed instantiations (frame / term / solution / research implication) plus one presentation rule would say the same thing with a third of the surface.

**F-08 (H) — ~30 named runtime categories, none instrumented.**
3 modes + 11 interaction moves + 6 shared-language micro-moves + 5 human contributions + 5 routing dimensions + 3 status ladders (5+6+5 values). A binding must decide, per turn, where it is in all of them. Two specific symptoms: `MAINTAIN` sits in the same taxonomy as `ELICIT` and `DECIDE` although `02` §8 says maintenance should be invisible and un-approved; and `CLARIFY_MEANING` overlaps `REFLECT_SOURCE` / `SEMANTIC_PROBE` from a different list. This is the main reason the protocol is currently hard to implement *and* hard to test: there is no declared core.

**F-09 (H) — The evaluation design cannot run at the available sample size.**
`05` specifies 7 core signals, 6 shared-language diagnostics, and 10 priority experiments, then §9 defines Keep/Investigate/Revert rules that presuppose comparative inference across runs. With n≈1 practitioner and runs measured in weeks, no Pareto comparison over 7 dimensions will ever be decidable, and E-05 already concedes that practitioner learning confounds run-over-run comparison. As written, the evaluation layer will produce numbers that cannot license its own decision rules. A defensible n=1 design is different in kind: pre-registered predictions, falsification criteria, and a small number of qualitative discriminating observations — not a metric dashboard.

### 3.3 Unsupported certainty and evidence handling

**F-10 (H) — The curated layer drops the strongest disconfirming study.**
As noted in §2.3: Shin et al. (CHI 2025, N=280) — no problem-frame quality improvement from LLM support, widened competence gap, lower perceived agency in novices — exists only in the German raw research. `research/01` §2 "Strongly supported directions" instead carries "Structured scaffolding can outperform generic chat" (Supermind Ideator, an *ideation* task). The pack's rule that "a claim in a normative file is not evidence for itself" is respected; the complementary rule — *curation must not filter out the closest counter-evidence* — is not. On current evidence, the honest headline is: **the closest study to this project's target task found no benefit, and the protocol is a bet that interaction design is what makes the difference.** That is a defensible and interesting bet. It should be stated as one.

**F-11 (M/H) — Two incompatible evidence-strength vocabularies.**
`source-research` uses *hoch / mittel / fundiert-theoretisch / emerging* with explicit definitions. Case 02's ledger uses *High / Medium / Low* where "High" means "clearly observed in this single, self-authored, dependent case". A reader — or a future agent — will read "Evidence strength: High" on E-02-01..E-02-07 as strong evidence for the rule. Case 02 §16 corrects this in prose, 500 lines later.

**Sharper instance of the same defect, added after review:** `source-research/01` rates the Supermind Ideator / scaffolding evidence *mittel* and explicitly *widersprüchlich*. `research/01` §2 promotes the same evidence to "**Strongly supported** directions". That is strength inflation happening inside the curation step itself, on the claim that most directly supports the project's premise — a more concrete example than the ledger-vocabulary one above, and it belongs with F-10 rather than beside it.

**F-12 (M) — Zero citations have been independently verified.**
The pack says citations must be verified before publication, which is right, but no file states the current status plainly: every reference in `source-research/` comes from a single Deep Research pass, carries internal `citeturn…` markers, includes several 2026-dated items and at least one arXiv preprint, and at least one entry (Noy & Zhang) has no DOI. Fabricated or drifted citations are a known failure mode of that production method. Until re-opened, *every* literature claim in this pack — including the ones I relied on in §2.3 — is unverified.

**F-13 (M) — `05` silently narrows the researched metric set.**
`source-research/03` recommends nine core metrics; `05` §3 carries seven, dropping *Discovery Quality Profile* and *Beneficial AI Uptake / Defective AI Resistance* — while `05` §9 still uses "defective-AI resistance" in the Keep/Investigate/Revert rule, i.e. a decision rule referencing a signal the protocol no longer collects. Narrowing may well be right (both dropped metrics need an independent reviewer), but the delta is undocumented.

### 3.4 Hidden assumptions

**F-14 (H) — The configuration is never declared: one human, one AI, one long conversation, no third parties.**
No stakeholders, no team, no client, no deadline, no budget, no parallel engineering. This assumption is load-bearing everywhere (turn economics, attention scarcity, decision rights, handoff), and it is nowhere stated. It is most acute in the shared-language layer, whose entire evidence base — Ubiquitous Language, common ground, lexical entrainment, conceptual pacts — is about *multi-party* alignment. In a 1:1 human–AI dyad where one party has no persistent memory and no stake, "shared language" may be a different phenomenon with a different failure profile.

**F-15 (M/H) — Every safeguard against AI anchoring is executed by the AI.**
Candidate-vs-canonical status, "do not present exploratory structure with convergence certainty", "surface consequential ambiguity", "do not silently commit" — all are model self-restraint against a failure mode (fluency → repetition → implicit commitment) that models are structurally poor at detecting in themselves. The protocol never names a single deterministic enforcement point outside the model. For a binding this is the key design question, and it is invisible in v0.2.

**F-16 (M) — Discovery is assumed to terminate in a handoff to a different implementation context.**
True in Case 01 and Case 02; not true of most product work, where the same people continue into build. §14's readiness definition and the cold-start test both depend on it. Either declare it as scope, or state what readiness means when discovery flows continuously into implementation.

**F-17 (M) — Model and harness invariance is assumed.**
The whole baseline was produced with ChatGPT-family models and Deep Research (inferable from Case 01's text; never stated). The protocol's central risk claim is a claim about *model behavior*. Case 03 is likely to run on a different model family in a different harness, which makes model family an uncontrolled variable in the first prospective test. `research/01` §7 lists portability as untested but does not treat it as a design variable.

**F-18 (H, cheap) — The protocol does not apply its own Analogy Boundary Check to its own imports.**
§11 mandates the check for any imported framework. v0.2 imports at least four: DDD / Ubiquitous Language (multi-party, code-bearing, long-lived teams), common ground & lexical entrainment (human–human dyads, referential tasks), *Turn* (predominantly autonomous implementation agents), and cognitive forcing functions (single-decision AI-advice settings). No analogy record exists for any of them. Case 02 identified analogy over-assimilation as a real failure that already happened once in this project.

### 3.5 Overfitting to the two dependent cases

**F-19 (H) — v0.2 is shaped by Case 02, and Case 01's operational layer was dropped without a recorded disposition.**
Case 01 does not merely contain observations. It contains a complete *Discovery Method v0.1*: phases M1–M8 with explicit exits, decision gates G1–G7, learning loops L1–L5, a four-way external-verification typology, stop conditions (including an explicit "probably overthinking" condition), anti-patterns AP-01..AP-10, and a twelve-item learning backlog. Protocol v0.1/v0.2 carries almost none of it: no gates, no stop conditions beyond prose, no review typology, no anti-pattern register, phases replaced by three modes.

Some of that was surely deliberate (phase machines conflict with co-evolution). But **no file records the disposition**, so a reader cannot tell what was rejected from what was forgotten. Concretely, several dropped items look stronger than things v0.2 kept:

- G3 *Information Loss Gate* + L3/M-05 *source / canonical / derived* — Case 01 explicitly flags this as a generalizable AI-discovery pattern. v0.2 rediscovered a narrow version (`source_expression`) via external research, and only for terminology.
- G6 *Review Gate* + M-03 *two reviews beat one* → see F-02.
- L9/M-12 *formal stop criterion instead of "it feels round"* → v0.2 has readiness prose, no gate.
- AP-10 / M-10 *artifact version churn* → absent, although the pack is itself a pile of versioned artifacts.

The net effect: the *object-level* case — the only one that is not about discovery methodology, and therefore the least self-referential evidence available — contributed the least normative content, while the meta-level, self-authored, dependent case contributed the most.

**F-20 (M) — Mechanisms tuned to one strong-willed expert practitioner.**
"Criticism surface" works because the human in both cases pushes back hard, repeatedly, with domain expertise. Shin et al. suggests the opposite population exists and behaves differently (novices lose agency and accept more). "Framing correction is the highest-value human act" generalizes the same person's strength. "Human attention is scarce" (D-04) is a design driver derived from one person's circumstances. "Deferral is cheap" holds when nobody is waiting on the decision.

**F-21 (M) — "Discovery" implicitly means greenfield conceptual design.**
Both cases are greenfield. Nothing addresses discovery inside an existing system, with legacy constraints, existing users, migration, or data that already encodes prior decisions — where "reopening the frame" is not cheap.

### 3.6 Gaps

**F-22 (H) — The commitment act is undefined.** See §2.5. `02` §11 requires that promotion to commitment need an "explicit transition"; nothing defines the transition, its fields, its owner, or how a commitment is revoked or superseded.

**F-23 (M/H) — No object for unresolved disagreement or AI dissent.**
Case 01 names *Confirmation Bias im normalen Chat* as an observed problem and AP-02 *Friendly AI Consensus* as an anti-pattern. `03` requires the AI to challenge — but if the human overrules the challenge, nothing records it, and the dissent does not survive into the handoff. This is also the cheapest partial substitute for the missing adversarial gate (F-02).

**F-24 (M) — No treatment of context limits, session boundaries, cost, or state growth.**
External state exists *because* context is lost, yet nothing specifies what happens at a session boundary, what must be re-loaded, how state is compacted, or what it costs. `05` mentions AI latency once.

**F-25 (H) — No conformance definition.** See T-11. Without it, "we ran Case 03 under Protocol v0.2" is not a checkable statement, and E1–E10 cannot be attributed to the protocol rather than to the practitioner.

### 3.7 What holds up well (fair-review counterweight)

- The evidence layering, and the rule that a normative claim is not evidence for itself.
- Case 02A's refusal to retro-fit shared-language evidence onto a retrospective written before that lens existed. This is better epistemic practice than most published method work.
- Case 02 §16's explicit "what this does not prove" list.
- `Meaning before naming → meaning before commitment` is a documented case of research overturning the project's own prior rule. That is the pack's best evidence that the learning loop is real.
- Refusing a composite score, and refusing "human token share" as an agency proxy.
- The decision-rights asymmetry (`03` §§3–7) is the most implementable part of the protocol and needs the least work.

---

## 4. Priority ranking of findings

If only five things are fixed before Case 03: **F-02** (adversarial gate), **F-25 + F-22** (conformance + commitment act), **F-08** (declare a core), **F-09** (evaluation that works at n=1), **F-10/F-11** (evidence honesty in the curated layer).

---

## 5. Change proposals

None of these are applied. Each states rationale, evidence, risk, and when it should be decided.

### CP-01 (High) — Make adversarial challenge a convergence gate, not only a release gate
**Change:** add to `01` §13 a condition — *"the current model has survived at least one deliberate attempt to break it, by a party or context independent of the pair that built it"* — and add a short review typology to the protocol: exploration review (what perspective is missing) / adversarial review (where does the model break) / verification review (are the named blockers actually closed) / spike (how does the external world behave). Keep §15 as the *release* instance of the same mechanism.
**Rationale/evidence:** Case 01 Phase 9, G6, L4, lessons L5 and M-03; Case 02 E-02-20 (the pack's most-cited own defect). This is the only mechanism supported by both cases *and* by a concrete before/after outcome (broad review → precision, not redesign; narrow review → stop).
**Risk:** ritualization; "independent reviewer" is expensive and may not exist. Mitigate with Case 01's own G6 threshold: review when the model is coherent, concrete enough to attack, and still cheap to change.

### CP-02 (High) — Remove the problem/solution split from the mode names
**Change:** either (a) rename to `EXPAND` / `CONVERGE` with an attribute `focus: problem | solution | both`, or (b) keep three modes but state explicitly that a mode names the *dominant learning objective of the moment*, never a phase, and that mode switches are expected many times per session.
**Rationale:** removes F-01; (a) also removes one taxonomy level, helping F-08.
**Risk:** loses vocabulary already used in `02` and in Case 02; renaming has a real cost. (b) is the low-cost option.

### CP-03 (High) — Replace the self-judged Independent-Position trigger with an enumerated event list
**Change:** in §4.3, replace "whether a strong AI anchor would destroy information worth observing" with a small closed list of anchor-risk events, e.g.: first framing of a newly opened object; selection among materially different directions; naming of a framing-bearing concept; statement of a high-impact criterion or priority; any decision the human will have to defend later without the AI present. Keep "not a universal human-first mandate".
**Rationale:** F-03. Also makes E2/H-02 testable — compliance becomes observable.
**Evidence:** the timing evidence (LLM before vs after independent ideation) is about *sequence at specific moments*, which is what a list encodes; it does not support a general "AI holds back" rule.
**Risk:** the list will be wrong at first. That is acceptable — a wrong list is revisable; an unobservable rule is not.

### CP-04 (Medium) — Collapse the four tentativeness devices into one ladder
**Change:** state Progressive Commitment once, with typed instantiations (frame / term / solution object / research implication) and one presentation rule ("render status honestly: exploratory structure must not carry convergence rhetoric"). Demote §6 to guidance under it; keep `02` §7 as the state encoding of the same ladder.
**Rationale:** F-07. Reduces surface without losing a distinction.
**Risk:** §6's exploration/convergence distinction is genuinely useful; it must survive as a rendering rule, not disappear.

### CP-05 (High) — Add a recorded-disagreement object
**Change:** add to state and to the handoff a small object: `challenge` — what the AI (or a reviewer) contested, the human's response, resolution status (`accepted / overruled / deferred / unresolved`), and whether it remains open at handoff.
**Rationale:** F-23; Case 01 AP-02 and the confirmation-bias observation. Cheapest available counterweight to a two-party echo chamber, and it makes "the AI challenged" verifiable rather than aspirational.
**Risk:** could become a complaint log. Bound it to high-impact decisions only.

### CP-06 (High) — Define the commitment act
**Change:** specify that a commitment exists only as an explicit recorded transition carrying: object, owner, date, the alternative rejected, the reason, the evidence/assumption it rests on, and the condition under which it should be revisited. No other route creates a commitment.
**Rationale:** F-22. This is the minimum deterministic anchor a binding needs, and it converts D-08 from a principle into something a hook or file schema can enforce (F-15).
**Risk:** friction if applied to everything — apply only to the `commitment` tier, not to decisions.

### CP-07 (High) — Reinstate disconfirming evidence in the curated layer
**Change:** add Shin et al. and the negative/null findings to `research/01` §2, and add a standing section *"Evidence against this protocol's premise"* that any future research pass must fill or explicitly mark empty.
**Rationale:** F-10. Also protects the project reputationally: a public method document that omits the closest null result invites exactly the criticism the project is trying to earn immunity from.
**Risk:** none I can see, beyond a less confident-sounding README. That is the point.

### CP-08 (Medium) — One evidence-strength scale, two columns
**Change:** harmonize the vocabularies across `evidence/` and `research/`, and in evidence ledgers split the single strength column into **observation clarity** (how clearly was this seen in this case) and **evidential weight** (what does it license for the protocol). Re-label Case 02's ledger accordingly.
**Rationale:** F-11.
**Risk:** editing an existing evidence case — do it as an added column and a dated note, never by rewriting the original judgements.

### CP-09 (Medium, cheap) — Analogy records for the protocol's own imports
**Change:** add an appendix with a completed `analogy` record (per `02` §10) for DDD/Ubiquitous Language, common ground/lexical entrainment, Turn, and cognitive forcing functions.
**Rationale:** F-18; self-application of §11. Also the fastest way to discover whether the shared-language layer is over-imported from multi-party settings (F-14).

### CP-10 (High) — Case 01 method disposition table
**Change:** add a table mapping every Case 01 method element (M1–M8, G1–G7, L1–L5, AP-01..AP-10, M-01..M-12) to `kept / transformed into X / deliberately dropped because Y / not yet considered`.
**Rationale:** F-19. Without it, nobody can tell rejection from oversight, and the strongest object-level evidence stays stranded in a 2,300-line German document.
**Risk:** may surface more re-additions than expected. That is a benefit, not a cost.

### CP-11 (High) — Declare Protocol Core vs Protocol Extended, and one hypothesis register
**Change:** split v0.2's content into (a) **Core** — conformance-defining, must be implemented and observable in any binding; and (b) **Extended** — experimental mechanisms explicitly not required for conformance. Merge the five hypothesis ID spaces into one register with a stable ID per hypothesis, its status, its owning document, and its falsification criterion.
**Suggested Core, for discussion:** commitment ladder + recorded commitment act (CP-06); epistemic vs decision status separation; deferred-decision register; persistent state with the nine integrity requirements; decision-rights tiers (`03` §§3–7); adversarial gate (CP-01); recorded disagreement (CP-05); handoff/cold-start artifact.
**Everything else Extended,** including the concept lifecycle, provenance labels, routing dimensions, move taxonomy, probe debrief ritual, and turn economics.
**Rationale:** F-08, F-25, and the ID sprawl noted in §2.2. This single change is what makes a minimal binding and a legitimate Case 03 possible.

### CP-12 (High) — Define conformance and a minimal trace
**Change:** add `T-11` conformance rules ("a run is v0.2-Core-conformant if …") and `T-12` a minimal event vocabulary (object created / status changed / deferred / challenged / committed / concept reopened / research delta recorded), timestamped and append-only.
**Rationale:** F-25, F-09; converts evaluation from dashboard aspiration to something derivable from a log.

### CP-13 (Medium) — Redesign evaluation for n=1
**Change:** replace the run-level metric dashboard as the *primary* instrument with: pre-registered hypotheses (max 5 per case) + predicted observable + falsification criterion, plus three cheap always-on measures (cold-start handoff blockers; decision explainability on 3 sampled decisions; state-integrity defects derivable from the trace). Keep the rest as an explicitly optional diagnostic catalogue. Restate Keep/Investigate/Revert as rules over pre-registered predictions, not over cross-run Pareto comparison.
**Rationale:** F-09, F-13 (and E-05's own concession about practitioner learning).
**Risk:** less impressive-looking evaluation section; far more likely to actually produce a defensible conclusion.

### CP-14 (Medium) — State the configuration assumption explicitly
**Change:** add to `01` §1 a declared scope: *one human, one AI, single-threaded discovery, terminating in a handoff to a separate implementation context*, plus a short "known untested extensions" list (teams, multiple stakeholders, discovery inside an existing system, continuous discovery→delivery).
**Rationale:** F-14, F-16, F-21. Also makes it honest to import multi-party evidence, by naming the transfer as a transfer.

### CP-15 (Low/Medium) — Context-scope the concept status; move turn economics to binding guidance
**Change:** (a) make shared-language `status` a per-context field, or state that one entry = one context. (b) `02` §5 (turn economics: "What changed / Why it matters / What is needed next") is a response-format rule — binding guidance, not technology-independent semantics. Same for the YAML blocks, which despite the disclaimer read as a serialization contract.
**Rationale:** F-05, and layer hygiene per D-02.

---

## 6. Questions that genuinely block the next phase

Only these four actually block. Everything else I can proceed on with a stated assumption.

**Q1 — Is there a real, available discovery to run as Case 03, and in what domain?**
Not Cookframe, not discovery-method design. If no real project exists in the next weeks, Case 03 becomes a simulation and produces non-evidence — which would make almost all of `05` and the entire learning loop unfalsifiable for another cycle. If none is available, the next phase must be designed differently (retrospective re-analysis of Case 01 under v0.2 semantics, or a deliberately small bounded case), and I would want to know that before proposing anything.

**Q2 — Who is v1 for: you alone, or third-party practitioners?**
This decides whether the protocol must be teachable and conformance-checkable (CP-11/CP-12 become mandatory, and F-20's population question becomes central), or whether it can remain a personal instrument that is merely *published*. It also decides how much of the public-project work in handover §6 is real work at all.

**Q3 — Is the harness/model change part of the experiment or a confound to control?**
The baseline was produced with ChatGPT-family models; Case 03 will presumably run in Claude Code. If model family is uncontrolled, some v0.2 mechanisms may be answering a failure profile that a different model exhibits differently (F-17). Options: accept and document; run Case 03 on the original family; or run a small paired probe.

**Q4 — What is publishable from `evidence/`, and in which language?**
Case 01 is a 2,300-line German document about a real product (Cookframe) with named third-party services. Is the product yours; is any of it confidential; is translation in scope; may it be published as an edited case or only as internal evidence? This gates handover task 3 and also gates CP-10's usefulness to any external reader.

### Decisions needed soon, where I will assume a default unless corrected

- **Enforcement posture.** I will assume: *deterministic external enforcement for status transitions and state integrity; advisory/prompt-level for everything else.* (F-15.)
- **Q6 — reviewer independence.** §15/D-21 require an independent adversarial review. This document is not that: same technology class, no separate evidence access. I will assume "independent" means *a different session with no access to this conversation, ideally a different model family, and at least one human reader* — but if you intend §15 to be satisfiable only by a human reviewer, say so, because that changes the release plan.
- **Effort/cadence.** No time, budget or cadence constraints appear anywhere in the pack; I will assume a solo practitioner working in bounded sessions and will size proposals accordingly.

---

## 7. Recommended next concrete phase

**Recommendation: do not proceed to handover tasks 2–5 as written. Run one phase whose only goal is to make v0.2 testable, and defer all public-project design until after Case 03.**

Rationale, in the protocol's own terms: repo topology, project name, README architecture and binding architecture are *commitments*, and the evidence that should inform them does not exist yet. Handover §6 schedules them before the first prospective evidence. Committing them now is precisely the `plausible abstraction → polished formulation → repeated use → accidental commitment` sequence that `01` §3 warns about. The pack's own maturity note agrees: *make these mechanisms testable, not merely more elaborate.*

### Phase P1 — "Make v0.2 testable" (three workstreams, timeboxed)

**W1 — v0.2.1 consolidation (no new mechanisms).**
Apply the accepted change proposals only. Specifically: CP-11 (Core/Extended split + one hypothesis register), CP-12 (conformance + minimal trace), CP-06 (commitment act), CP-01 (adversarial gate), CP-05 (recorded disagreement), CP-14 (declared configuration), CP-07/CP-08 (evidence honesty), CP-09/CP-10 (analogy records + Case 01 disposition). Net effect should be a *smaller* normative document than v0.2, not a larger one. If v0.2.1 is longer than v0.2, the phase has failed.

**W2 — Thin instrument, not "the reference binding".**
Build only what makes Core observable: one persistent state file, one append-only event log, and the smallest set of operations that record status transitions, deferrals, challenges and commitments. Harness-specific, deliberately disposable, explicitly *not* the architecture. This is a probe, in the protocol's own vocabulary — it should carry a stated learning question and a discard condition.

**W3 — Case 03 pre-registration, frozen before the discovery starts.**
Domain and object; declared Core conformance; at most five hypotheses with predicted observables and falsification criteria (my suggested five: criticism surface, enumerated human-first events per CP-03, external state, candidate-first terminology, adversarial gate); the trace plan; the cold-start handoff test design and who runs it. Frozen and committed before the first discovery turn — that freeze is what converts the pack's retrospective evidence into prospective evidence, and it is the single highest-value thing this project can do next.

**Explicitly deferred through P1:** T-01 (name), T-02 (topology), T-05 (skill/hook architecture), T-06 (review UI), T-07 (evaluator architecture), T-08 (release workflow), and all public README/IA work.

**Exit criteria for P1:**
1. v0.2.1 exists, is smaller, and its Core is stated as checkable rules.
2. A run can be shown to be Core-conformant or not, from its trace alone.
3. Case 03 pre-registration is frozen, with falsification criteria that could actually come out negative.
4. One independent adversarial pass on v0.2.1 (per Q6) has happened — this document does not count.

**If Q1 comes back negative** (no real Case 03 domain available): substitute W3 with a re-analysis of Case 01 under v0.2.1 Core semantics — i.e. replay the Cookframe discovery as a conformance and expressiveness test of the protocol, which would at minimum test whether v0.2 can *describe* a real object-level discovery. That is weaker evidence, but it is not fake evidence.

---

## 8. Evaluation of the handover itself

The handover is unusually good at stating what is *not* proven. It is weak at stating what exists, what was rejected, and under what conditions the work was produced. Concretely, here is what I had to rediscover, infer, or guess.

### Had to rediscover
1. **Case 01 contains a complete method (M1–M8, G1–G7, L1–L5, AP-01..AP-10, M-01..M-12), not just a retrospective.** The handover describes it in one line: *"A long product discovery produced an implementation handoff."* This concealed the single largest traceability gap in the pack (F-19) and is the one thing I would most want fixed in the next handover.
2. **Case 01 and all four `source-research` reports are in German**; `protocol/`, `research/` and Case 02 are in English. Stated nowhere. It has direct consequences for publication, external review, and citation verification effort.
3. **The strongest disconfirming study in the pack** (Shin et al.) exists only in the raw German research and never propagates upward (F-10). Nothing in the handover flags that curation dropped counter-evidence.
4. **`05` narrows the researched metric set** while keeping a decision rule that references a dropped signal (F-13).
5. **Five separate hypothesis ID spaces** that partly duplicate each other. I had to reconcile them by hand to answer the handover's own question 2.

### Had to infer
6. **Production conditions:** ChatGPT-family models plus a Deep Research tool, inferred from Case 01's prose. Never stated as a fact about the baseline, and it is a controlled variable for any future comparison (F-17).
7. **Configuration:** one human, one AI, solo practitioner, no team, no client, no deadline. Load-bearing everywhere, declared nowhere (F-14).
8. **That the practitioner, protocol author, evidence analyst and evaluator are the same person.** This is the central threat to validity in the whole evidence apparatus and the handover never names it.
9. **Deliverable form for this task.** Handover §5 says "produce an orientation" and "perform a review" but not what artifact results, where it belongs in the layer model, or whether it is meant to be public. I placed this at project-input level next to the handover; that was a guess.
10. **Whether v0.2's omissions were decisions.** With no "considered and rejected" record, I could not distinguish a deliberate simplification from a loss (F-19).

### Had to guess
11. **Effort, budget and cadence.** No constraints stated anywhere.
12. **Whether Case 01's product (Cookframe) is publishable at all** — ownership, third-party material, confidentiality (Q4).
13. **What "independent" means for the D-21 review** — different session, different model, or a human (Q6).
14. **The intended relationship between "protocol" and "binding" beyond the README paragraph.** *Binding* is itself an un-canonicalized model-bearing term, which the pack's own `04` policy would flag: it is used normatively across five documents with no entry, no definition of what makes something a binding rather than a usage, and no boundary test.

### What the baseline should carry next time
A one-page **baseline fact sheet**: document languages; production tooling and model family; dates; who the practitioner is and their relation to the evidence; citation verification status (currently: none verified); one hypothesis register; a "considered and rejected" record; and a definition of the deliverable expected from the next agent. Eight of the fourteen items above would disappear.

### One structural criticism of the handover
Tasks 1–5 are a waterfall: orient → design the public project → evidence hygiene → research implementation options → implementation-discovery proposal → then evidence. The protocol these tasks serve says *commitment late, probes early and reversible*, and that structure for exploration must not be confused with structure for convergence. The handover's own task ordering front-loads the most committing, least reversible decisions (project name, repo topology, public IA) before the first prospective evidence exists. That is worth noticing precisely because it is the failure mode the protocol was written to prevent — which is also mild evidence for the protocol's central claim.
