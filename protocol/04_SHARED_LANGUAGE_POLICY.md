# Shared Conceptual Language Policy v0.2

> **Status:** experimental, protocol v0.2. Rules may still change between versions.

## 1. Purpose

Long-running Human–AI discovery benefits from shared vocabulary.

But a common word does not guarantee common meaning.

AI systems create an additional risk because they can transform fuzzy human language into fluent abstractions and professional terminology almost instantly.

The policy therefore aims to preserve the benefits of shared language without treating AI naming as automatic conceptual agreement.

---

## 2. Core rule

> **For model-relevant concepts, preserve the human source meaning, treat AI names as proposals, test meaning in use before stabilization, and keep shared language explicitly revisable.**

Short form:

> **Meaning before commitment.**

Not:

> Meaning before every possible name.

Early names may help thinking.

What must be delayed is **implicit commitment to the model carried by the name**.

---

## 3. What counts as model-relevant language?

Use explicit terminology handling only if a different interpretation could change:

- requirements;
- decisions;
- domain boundaries;
- responsibilities;
- priorities;
- architecture-relevant conceptual boundaries;
- evaluation;
- handoff meaning.

If not, keep talking normally.

---

## 4. Source meaning

When a human introduces an important concept in fuzzy, local or metaphorical language, AI should avoid immediately erasing that source.

Useful source material may include:

- original phrase;
- concrete example;
- local stakeholder term;
- metaphor;
- exception;
- stated purpose.

Source language is evidence about how the problem is currently understood.

It is not automatically the final canonical vocabulary.

---

## 5. AI naming as proposal

AI may propose terminology early when it helps:

- compress discussion;
- expose a distinction;
- provide established domain language;
- articulate a fuzzy intuition;
- compare alternative models.

For important concepts, prefer:

> "A possible term is X; it implies Y."

over:

> "We call this X."

---

## 6. Candidate terms as semantic probes

Terminology can be used as a probe.

Example:

```text
"State" suggests a coherent current condition.

"Memory" foregrounds retention, retrieval, forgetting and update.

"Ledger" foregrounds durable records and traceability.
```

The point is not "which word sounds best?"

The point is:

> **Which conceptualization matches the thing we are actually trying to model?**

Offer a small number of candidates with materially different implications.

Avoid synonym dumps.

---

## 7. Lightweight lifecycle

The exact lifecycle is experimental, but v0.2 uses this working model:

```text
SOURCE MEANING
→ CANDIDATE TERM
→ WORKING TERM
→ CANONICAL-FOR-NOW
→ REOPEN / RENAME / SPLIT / MERGE / DEPRECATE
```

### Candidate
Useful language proposal; no implied acceptance.

### Working
Convenient shared label currently used while meaning may still evolve.

### Canonical-for-now
Stable enough for the current context, decisions and handoff.

This does **not** mean globally true or immutable.

### Reopened
New evidence or scenarios show the meaning needs revision.

---

## 8. Semantic testing

For consequential concepts, use one or more lightweight tests:

- clear example;
- non-example;
- edge case;
- second workflow;
- compare consequences of two interpretations;
- human paraphrase in their own words.

Do not turn this into a mandatory ritual for every word.

A definition alone is insufficient evidence of shared understanding.

---

## 9. Context boundaries

Do not force one global term when local meanings are legitimate.

A term may be:

- canonical in Billing;
- different in Identity;
- intentionally ambiguous at system level.

Context collision can be solved by explicit context boundaries rather than forced lexical uniformity.

---

## 10. Revisability

Renaming is not automatically a failure.

A rename, split or merge can be evidence that the model improved.

What is more concerning:

- late surprising rename;
- downstream decisions built on an untested meaning;
- a glossary that stays stable while real usage changes.

Usage and new evidence may reopen the concept.

---

## 11. Minimal shared-language state

Only for model-relevant concepts:

```yaml
term:
meaning:
status:
context:
source_expression: optional
provenance: optional
example_boundary: optional
open_issue: optional
rename_history: only if meaningful
```

Avoid:
- full conversation duplication;
- exhaustive synonym history;
- terminology objects for every specialist word.

---

## 12. Provenance

Possible origin values:

- Human
- AI
- External domain language
- Co-constructed

Explicit provenance is **experimental**.

It may improve traceability and ownership, but it may also create new attribution bias.

Do not make visible provenance mandatory until tested.

---

## 13. Relation to Human Contributions

### Situated Grounding
Source expressions and local terms can contain evidence.

### Framing & Meaning
Terms may imply category boundaries and causal models.

### Independent Position / Authorship
For framing-bearing terminology, preserving human meaning before strong AI naming can retain useful independent information.

### Judgment & Exceptions
Counterexamples are a strong semantic test.

### Commitment & Accountability
Canonicalization of a high-impact term can be a small model commitment.

Shared Language is cross-cutting; it is not a sixth Human Contribution.

---

## 14. Failure modes

### AI terminology anchoring
Elegant term becomes default before model implications are examined.

### Lexical alignment without conceptual alignment
Both sides repeat the same word but classify cases differently.

### Premature canonicalization
Tentative concept receives status too early.

### Source erasure
AI paraphrase replaces a human phrase carrying important purpose/context.

### Semantic drift
Meaning changes while the word stays stable.

### False precision
Language becomes cleaner faster than understanding.

### Jargon inflation
AI invents unnecessary professional vocabulary.

### Vocabulary bureaucracy
Terminology maintenance consumes more cognition than it saves.

### Suppression of useful ambiguity
A distinction is forced before a decision actually depends on it.

---

## 15. Experimental mechanisms

Still hypotheses:

- explicit provenance labels;
- mandatory candidate/working/canonical status UI;
- scenario gate before canonicalization;
- short independent human articulation before framing-bearing AI terminology;
- concept registry outperforming high-quality implicit memory.

These belong in the Learning Backlog, not as universal best practice.
