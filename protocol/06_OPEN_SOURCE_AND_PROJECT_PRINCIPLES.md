# Open-Source & Project Principles v0.2

## 1. Intent

The future project should be suitable for public GitHub development.

Public work can:
- make the protocol useful to others;
- attract critique and contribution;
- make method evolution inspectable;
- demonstrate rigorous working practice through the quality of the work itself.

The README should lead with usefulness, not personal portfolio motivation.

---

## 2. Public artifact rule

> **Anything committed publicly should be treated as a durable public artifact.**

Includes:
- docs;
- issues;
- PRs;
- commit messages;
- code;
- tests;
- evaluation results;
- evidence cases.

Avoid:
- private personal context;
- confidential client/company details;
- private chat transcripts;
- secrets;
- unstable internal research citations presented as public evidence.

---

## 3. Protocol and implementation evolve independently

Separate:

### Normative protocol
What Human–AI Discovery should do.

### Binding/reference implementation
How a given environment realizes it.

Harness limitations must not silently rewrite the protocol.

Protocol changes need not force every binding to update immediately.

---

## 4. Repository topology remains open

Evaluate:

- monorepo;
- protocol repo + binding repos;
- hybrid.

Criteria:
- discoverability;
- conceptual clarity;
- independent versioning;
- contribution boundaries;
- release cadence;
- test/evaluation ergonomics;
- implementation coupling;
- maintenance overhead;
- maturity visibility.

---

## 5. Public information architecture

The public entry point should answer:

1. What problem does this solve?
2. Who is it for?
3. What is the protocol?
4. What is implemented?
5. What is experimental?
6. What evidence exists?
7. What can someone try today?
8. How can they contribute evidence or implementation?

Show protocol maturity separately from implementation maturity.

---

## 6. Public context should be identified early

If a discovery is likely to become public/open source, capture that constraint early enough to affect:

- privacy boundaries;
- terminology;
- artifact design;
- evidence hygiene;
- source/citation strategy.

But do not let portfolio/publication concerns prematurely optimize for polish over learning.

---

## 7. Research publication hygiene

Before publishing evidence claims:

- replace internal ChatGPT citations;
- verify primary sources;
- mark peer-reviewed vs preprint vs practitioner;
- distinguish research result from protocol inference;
- avoid inflated "validated" language.

---

## 8. Evidence cases

Evidence Cases can be public artifacts, but should be edited for:

- self-contained context;
- privacy;
- non-circular evidence logic;
- traceable observations;
- clear dependence between cases;
- claims proportional to evidence.

Raw retrospectives and raw Deep Research outputs are source materials, not automatically publication-ready.

---

## 9. Versioning

Where useful, version independently:

- Protocol;
- binding;
- evaluation schema;
- evidence case format.

Protocol releases should state:

- changed rule;
- evidence/observation motivating it;
- expected mechanism;
- known downside;
- unresolved hypothesis.

Method evolution itself is part of the product.
