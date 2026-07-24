# Core evolution: how concepts move from workspace to core

The Digicities ontology is intentionally minimal. Domain concepts are authored by partners in their own workspaces. Only concepts that prove broadly useful across multiple workpackages get promoted into core. This document describes the lifecycle and the contract it implies for downstream services.

## Where extensions live

Extensions live in **workspaces**, not in this repo. A workspace ships its own `ontology/extensions/*.ttl` files alongside its ingested data, scenarios, and queries. See the [REFORMERS workspace corpus](https://github.com/REFORMERS-EnergyValleys/REFORMERS_Ontology-Extensions-and-Knowledge-Graphs) for a real example.

Extensions use the **`dici_onto:` namespace** (`https://digicities.info/ontology#`), the same as core. Two reasons:

- SPARQL queries find core and extension terms uniformly. No UNION over multiple namespaces.
- Concepts that later get promoted to core don't change IRI. Workspace data and queries keep working unchanged.

The [validator](../tools/validate_extension.py) enforces this and a few other structural rules (parents declared, labels and comments present, no redefining of core terms).

## The three-stage lifecycle

```
┌─────────────────────┐   adoption    ┌─────────────────────┐   promotion   ┌─────────────────────┐
│ Workspace-local     │  ───────────► │ Multi-workspace use │  ───────────► │ Core release        │
│ (extensions/*.ttl)  │               │ (same IRI reused)   │               │ (dici_onto_core.ttl)│
└─────────────────────┘               └─────────────────────┘               └─────────────────────┘
```

### 1. Workspace-local

A partner mints a new class or property in their workspace's `ontology/extensions/<name>.ttl`. No central review, no PR queue. They run [`tools/validate_extension.py`](../tools/validate_extension.py) locally before committing to their workspace repo.

### 2. Multi-workspace adoption

Another partner finds the same concept useful. They reference the existing IRI in their own extension (since both target the shared `dici_onto:` namespace). No coordination through this repo. The convergence happens naturally as people copy what works.

### 3. Core promotion

Once a concept is in use across **≥2 workpackages**, a maintainer opens a PR against `core/dici_onto_core.ttl` adding it. The contributing partners' existing TTL data continues to work unchanged because the IRI didn't move. On their next core upgrade, they can drop the term from their local extension if they want. They don't have to.

Promotion criteria, in rough order of importance:

1. **In use across ≥2 workpackages.** Proves the concept generalises.
2. **Stable for ≥6 months.** Proves the definition has settled.
3. **No competing definition.** If two workspaces have inconsistent declarations, those need to be reconciled before promotion.
4. **The full annotation set is present and clean.** Core is a public artefact that both humans and onboarding agents map onto: every promoted term needs `rdfs:label` + `rdfs:comment`, and classes where mapping decisions happen also need `skos:definition`, `skos:altLabel` (synonyms), `skos:example`, and — where siblings could be confused — a `skos:scopeNote`. See [`AGENT_MAPPING_GUIDE.md`](AGENT_MAPPING_GUIDE.md). Sloppy prose stays in workspaces.
5. **The term index is regenerated.** Run `python tools/generate_term_index.py` and commit the updated `docs/term-index.{json,md}` — CI fails on a stale index.

## Service compatibility contract

A service (forecasting tool, scenario analyser, optimisation backend) is built against a specific snapshot of the shared vocabulary plus possibly some workspace extensions. The service author declares this explicitly so version drift is visible:

```yaml
# digicities-compat.yaml shipped with the service
core_version: ">=0.3.0,<1.0.0"
workspace_extensions:
  - id: example_workspace
    commit: abc1234
```

This says: *"My service expects Digicities core v0.3.x and the example_workspace workspace's extension as of commit abc1234."* If either changes in a breaking way, the version mismatch surfaces at integration time. The service author decides whether and when to update.

The mechanism for **automatically notifying** service authors that a concept they were carrying in their workspace extension has been promoted to core is deferred. See "Future work" below.

## Conflict handling (deferred)

If two partners independently mint the same `dici_onto:` IRI for different things, the conflict surfaces when their workspaces' graphs are queried together (federated SPARQL) or when one partner tries to reuse the other's extension. We expect this to be rare in practice. When it does happen, the partners coordinate directly.

The knowledge base does **not** try to prevent collisions upfront. Central enforcement would require a governance structure that doesn't currently exist, and the cost of getting it wrong (over-bureaucratising what should be a fast, contextual authoring process) outweighs the benefit. As the corpus matures and conflicts do start to appear in practice, a lightweight claims-registry layer can be added.

## Future work

These mechanisms are intentionally not built yet. Add them when the corpus is mature enough that they pay for themselves:

- **Claims registry.** A tiny `terms.csv` in this repo listing every `dici_onto:` IRI claimed by any workspace, with the workpackage owner. A pre-commit hook in workspaces could check it. Cheap, but only worth adding once collisions are an actual problem.
- **Promotion notification.** When a new core release lands, scan recent workspace extensions for terms that just moved into core, and ping the authors. Could be a one-shot script run by the maintainer when cutting a release.
- **Federation alignment.** When two workspaces are queried together, materialise `owl:equivalentClass` declarations to reconcile partner-specific subclasses that mean the same thing. Out of scope until services start needing cross-workpackage queries.

The intent of this document is to **leave room** for these mechanisms without locking them in prematurely. The corpus must mature. The governance has to follow the actual usage, not the other way around.

## See also

- [`CONTRIBUTING.md`](../CONTRIBUTING.md): how to open a PR against this repo (core changes, docs, tooling).
- [Extensions in a workspace](https://github.com/uesl-empa/digicities-platform/blob/main/docs/INFERENCE.md): how the platform loads core plus workspace extensions and materialises RDFS-Plus inference at workspace open.
- The [REFORMERS corpus](https://github.com/REFORMERS-EnergyValleys/REFORMERS_Ontology-Extensions-and-Knowledge-Graphs): a working example of partners authoring extensions in their workspaces.
