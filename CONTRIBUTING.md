# Contributing to the Digicities ontology

This repo holds only the **core** Digicities ontology: small, curated, versioned. Domain-specific extensions live in workspaces, not here. See [`docs/CORE_EVOLUTION.md`](docs/CORE_EVOLUTION.md) for the model and the workspace to core promotion lifecycle.

## What kinds of PRs this repo accepts

### 1. Promoting a concept from workspace extensions into core

The most impactful contribution. When a concept has been used in **≥2 workpackages** and proven stable for a few months, open a PR adding it to `core/dici_onto_core.ttl`.

The PR should:

- Add the class or property declarations to `core/dici_onto_core.ttl`. Use the existing structure as a guide. Group related concepts together. Keep labels and comments crisp.
- Carry the **full annotation set**: `rdfs:label`, `rdfs:comment`, and for classes `skos:definition`, `skos:altLabel` (synonyms), `skos:example`, plus a `skos:scopeNote` where the class could be confused with a sibling. These annotations are what onboarding agents map new usecases with — see [`docs/AGENT_MAPPING_GUIDE.md`](docs/AGENT_MAPPING_GUIDE.md). The tests enforce label/comment coverage.
- Regenerate the term index (`python tools/generate_term_index.py`) and commit the updated `docs/term-index.{json,md}` — CI fails on a stale index.
- Update [`docs/class-hierarchy.md`](docs/class-hierarchy.md) and [`docs/attribute-types.md`](docs/attribute-types.md) if you've added classes that belong in those lists.
- Link the originating workspace extensions in the PR description so reviewers can see the prior art.
- Note in the PR body which workpackages were using the concept and for how long.

Run `pytest` to confirm the core still parses cleanly.

### 2. Fixing core, docs, or tooling

A bug in a class definition, an out-of-date doc, a tooling improvement. Open a regular PR. Keep changes focused. One logical fix per PR.

### 3. Reporting collisions or conflicts

If you find that two workspace extensions have declared the same `dici_onto:` IRI with conflicting semantics, open an **issue** (not a PR) describing the conflict and which workspaces are involved. The knowledge base doesn't try to prevent collisions upfront. See the "Conflict handling" section of [`docs/CORE_EVOLUTION.md`](docs/CORE_EVOLUTION.md) for why. We'll triage and help the workspace authors coordinate.

## What goes in workspaces, not here

- New classes or properties that haven't yet been adopted by multiple workpackages. Author them in your own workspace's `ontology/extensions/`.
- Project-specific naming, taxonomies, conventions, or labelling. Keep them workspace-local.
- Tweaks to the rdfs:label or rdfs:comment of an existing core term to fit your project's wording. Override locally. Don't push project-specific wording into the shared vocabulary.

## Licensing of contributions

By submitting a contribution to this repository (core changes, docs, tooling), you agree that your contribution is licensed under [**Creative Commons Attribution 4.0 International (CC BY 4.0)**](LICENSE), the same license as the rest of the ontology.

This means:

- Others can freely use, redistribute, and adapt your contribution.
- They must credit the source, typically by linking back to this repo.
- You retain copyright in your contribution.

If your employer holds rights to your work, please confirm they're OK with you contributing under CC BY 4.0 before opening a PR.

## Code of conduct

Be kind. Disagreements about ontology design are normal. Argue about ideas, not people.

## Questions

Open a discussion or an issue. If you're not sure whether something belongs in core, in a workspace extension, or somewhere else entirely, ask first. It's much easier than redoing the work later.
