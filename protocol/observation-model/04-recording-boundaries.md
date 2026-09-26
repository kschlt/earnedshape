# Recording Boundaries

> **Status:** experimental, protocol v0.2.1. Rules may still change between versions.

> **Owns:** what an event may never contain.

The event stream is the raw material for cross-run analysis, and analysis output eventually leaves the private store as sanitized findings. Boundaries drawn at the point of *recording* are the only ones that hold; boundaries drawn at the point of publication are a promise that a tired person makes at the wrong moment.

## The rule

> **An event carries structure and references. It does not carry the discovery's content.**

A `commitment.recorded` event says that a commitment was recorded, by whom, against which rejected alternative, resting on which evidence references, revisitable under which condition. It does not say what was decided, in a domain, for a client.

References (`*_ref`) point into the private run store, where the content lives. The store is private; the event stream is *the thing designed to be analysable and, in aggregate and abstracted, publishable*.

## Never in an event payload

- verbatim conversation text beyond a bounded summary field
- domain content: product names, feature names, client or employer names, personal names
- credentials, tokens, hostnames, file paths that reveal a project
- anything that identifies a third party who did not consent to being recorded
- a `domain` string precise enough to identify the project — that field lives in the run record, in the private store, and never travels

## Bounded summaries

Where a summary is genuinely needed to make an event interpretable, it is:

- length-capped, and truncated rather than paraphrased when over;
- descriptive of the *move*, not the *content* — "human rejected the AI's framing of the primary actor", not the framing itself;
- marked `summary_source: model | human` because a model-written summary of a human's move is an interpretation, and interpretations drift.

## Why this is a Phase 0 decision and not a later one

Retrofitting boundaries onto an existing store means re-processing every historical event with a classifier that will miss things, and then living with the uncertainty about whether it missed something. Deciding now costs one document; deciding later costs the ability to publish anything derived from early runs.

The same reasoning applies to the run id (`01-run-record.md`): it is opaque because a sanitized finding cites it, and an id that encodes the project defeats the sanitization it is supposed to survive.

## What this does not solve

It does not make the event stream publishable as-is. Aggregate patterns can still identify a project — the timing of runs, the sequence of domains, the count of active projects. The stream stays private; only analysis output crosses, and only after review. This document narrows what has to be reviewed; it does not remove the review.
