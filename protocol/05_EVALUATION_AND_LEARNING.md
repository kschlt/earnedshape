# Evaluation & Learning Protocol v0.2.1

> **Status:** experimental, protocol v0.2.1. Rules may still change between versions.

## 1. Principle

The protocol itself is a versioned hypothesis.

Evaluate:

- discovery quality;
- human understanding/agency;
- state integrity;
- convergence quality;
- downstream handoff fitness;
- active human effort.

Do not optimize one composite score.

---

## 2. Primary instrument: pre-registered predictions

Evidence arrives one case at a time. At n=1 there is no population to compare against, so a run-level metric dashboard cannot be the primary instrument. Before each case, pre-register:

- **hypotheses** — at most five per case;
- **predicted observable** — what the run should show if the hypothesis holds;
- **falsification criterion** — what the run would show if it does not.

### Quality gates

#### Gate 1
Discovery/handoff quality must remain acceptable.

#### Gate 2
Human understanding/agency must not materially deteriorate.

The two gates still apply to every case. Cross-run Pareto comparison of state integrity, convergence, workload, active human time and process overhead becomes possible once several comparable cases exist; until then it is a diagnostic, not the verdict.

A faster protocol is not better if it produces more product rediscovery or weaker human ownership.

---

## 3. Always-on measures and optional diagnostics

Three measures are cheap enough to take on every run, whatever was pre-registered:

### Cold-Start Handoff Blockers
Can a fresh implementation context proceed using only the final discovery baseline?

### Decision Explainability Coverage
Can the human explain consequential decisions, alternatives, trade-offs and uncertainty without the original AI? Sample three consequential decisions per run.

### State-Integrity Defects
Lost decisions, contradictions, stale assumptions, missing provenance/status — derived from the trace, not from recollection.

The signals below form an **optional diagnostic catalogue**. Use one when a pre-registered hypothesis needs it; none of them is required.

### Useful Breadth before Commitment
Materially distinct frames/solution mechanisms considered before high-impact commitment.

### No-New-Evidence Reopenings
High-impact decisions reopened without meaningful new evidence, constraint, user information or error discovery.

### Active Human Time
Human work time separated from AI latency/calendar time.

### Workload / Agency Pulse
Short self-report.

---

## 4. Shared-language diagnostic signals

These are **experimental**, not core success metrics.

Potential observations:

### Late Concept Disagreement
A term previously treated as stable later reveals materially different meanings.

### High-impact Late Rename
A late rename/split changes downstream requirements, decisions or boundaries.

### Scenario Agreement
Human and AI independently classify new cases consistently under a shared concept.

### Independent Human Explanation
Can the human explain the concept and its boundary without copying AI wording?

### Source-Recovery Value
Did preserved source language later reveal a semantic drift or hidden intent?

### Terminology Burden
How much interaction/state overhead does explicit terminology management create?

Do **not** optimize:
- number of AI-originated terms;
- raw renaming rate;
- lexical alignment.

Those measures are ambiguous.

---

## 5. Research Model Delta

After research:

```text
Previous model
→ Evidence
→ REINFORCED / REFINED / CHALLENGED / NEW / NO CHANGE
→ decision impact
→ remaining uncertainty
```

Research quality should partly be judged by whether it resolves a meaningful uncertainty or changes the working model.

---

## 6. Short AAR

After each completed discovery:

1. Which 1–3 decisions were consequential?
2. Which can I explain and defend without the original dialog?
3. Where did AI meaningfully improve my model?
4. Where did I nearly accept AI too easily?
5. Which perspective/constraint/counterhypothesis arrived late?
6. Which iteration was unnecessary?
7. Which important concept/term was misunderstood, renamed or silently stabilized?
8. What one protocol change might have had the largest effect?

---

## 7. Protocol change template

```text
Observation:
Hypothesis:
Mechanism:
Expected effect:
Possible side effect:
Measures:
Decision rule:
```

---

## 8. Learning loop

```text
pre-registered predictions
→ real run
→ mostly automatic measurement
→ short AAR
→ protocol hypothesis
→ small change
→ several runs
→ pattern review
→ controlled comparison if needed
```

---

## 9. Keep / Investigate / Revert

Rules over the pre-registered predictions of §2, not over a cross-run comparison. Both gates of §2 must hold for **Keep**.

### Keep
The predicted observable appeared, the falsification criterion was not met, and the always-on measures (§3) showed no material defect: no cold-start blocker, the sampled decisions explainable, no systematic state-integrity defect.

### Investigate
The prediction held, but an always-on measure showed a material defect, or a diagnostic used for this hypothesis — for example breadth, understanding or semantic consistency — pointed the other way.

### Revert
The falsification criterion was met, or a gate of §2 failed: major handoff blockers, discovery reopenings, understanding loss or systematic state/concept defects.

---

## 10. Priority experiments from v0.2

### E1 — Criticism Surface
Incomplete working model vs polished model.

### E2 — Human-first Signal
Selective independent human articulation before strong AI anchor.

### E3 — Solution Probe + Debrief
Explicit probe lifecycle vs natural reflection.

### E4 — External Runtime State
Persistent state vs conversation-only reconstruction.

### E5 — Candidate-first Terminology
Candidate language vs silent canonicalization.

### E6 — Meaning-first selective terminology
Semantic probe → candidate → use-test for high-impact concepts.

### E7 — Source-preserving reformulation
Original phrase retained beside AI interpretation vs replacement.

### E8 — Analogy Boundary Check
Explicit non-transferability analysis vs analogy-only reuse.

### E9 — Exploration-turn brevity
Compact navigation turns vs repeated long synthesis.

### E10 — Bounded uncertainty readiness
Handoff with explicit technical deferrals vs more exhaustive discovery.

---

## 11. Independent Evidence Case 03

The next major evidence milestone should be a content-independent case.

Preferably instrument it **before** the discovery begins:

- protocol version;
- model/harness version;
- active state mechanism;
- pre-registered hypotheses, predicted observables and falsification criteria (§2);
- lightweight telemetry;
- AAR;
- planned cold-start handoff test.

The goal is to move from retrospective inference toward prospective evidence.

---

## 12. Evidence strength: one scale, two columns

Evidence records use one vocabulary for strength, and keep apart two things that a single column conflates. Older records keep their original labels and get the second column added (below).

### Observation clarity
How clearly was this seen in this case?

- `clear` — directly observed and recorded;
- `partial` — observed, but incompletely or only in part of the case;
- `inferred` — reconstructed after the fact.

### Evidential weight
What does it license for the protocol?

- `strong` — replicated, or several independent studies;
- `moderate` — one independent study, or consistent support from several weaker sources;
- `weak` — practitioner literature, a single dependent or self-authored case, or the project's own inference;
- `contested` — the evidence points in different directions.

Observation clarity never raises evidential weight: a clearly observed pattern in one self-authored, dependent case is still `weak` evidence for the protocol.

Existing evidence ledgers are not rewritten to fit. The second column is **added**, with a dated note, and the original judgements stay as they were recorded.
