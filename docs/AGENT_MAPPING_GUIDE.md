# Mapping domain concepts onto the Digicities ontology

This guide is written for **agents** (and humans) onboarding a new usecase:
you have domain concepts — `WindPark`, `ChargingStation`, `RoomTemperature` —
and must decide where each one hangs in the core ontology. **Never map by
name similarity alone.** Every core term carries machine-readable
annotations, and this guide is the procedure for using them.

## The annotation surface

Every term in `core/dici_onto_core.ttl` carries:

| Annotation | What it tells you |
|---|---|
| `rdfs:label` | Human-readable name |
| `rdfs:comment` | One-line description |
| `skos:definition` / `dici_onto:definition` | Precise meaning, boundary conditions |
| `skos:altLabel` | Synonyms — the words *your* domain might use for this concept |
| `skos:example` | Concrete instances/subclasses that belong here |
| `skos:scopeNote` | When to use this class **and when not to** (disambiguation vs. sibling classes) |

Two ways to read them:

1. **The term index** — [`docs/term-index.json`](term-index.json) (structured)
   and [`docs/term-index.md`](term-index.md) (greppable). One card per term
   with the full annotation set plus the parent chain to the root. Generated
   from the TTL — regenerate with `python tools/generate_term_index.py`; a
   workspace can pass its extension TTLs to get a combined index.
2. **SPARQL against the loaded graph** (the platform materialises core +
   extensions into each workspace's dataset, annotations included):

```sparql
PREFIX dici_onto: <https://digicities.info/ontology#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

# Which core class is known by the synonym "Site"?
SELECT ?cls WHERE { ?cls skos:altLabel "Site"@en }        # → dici_onto:Location

# Everything an agent needs to judge a candidate parent:
SELECT ?p ?o WHERE {
  dici_onto:Location ?p ?o .
  FILTER(?p IN (rdfs:comment, skos:definition, dici_onto:definition,
                skos:altLabel, skos:example, skos:scopeNote))
}
```

## The mapping procedure

For each domain concept:

1. **Search the term index** for the concept's name, its synonyms, and the
   words the model's documentation uses. Check `altLabels` and `examples` —
   a hit in `examples` ("A wind park, a city district, …") is a strong signal.
2. **Read the `scopeNote`** of every candidate — scope notes exist precisely
   to break ties between sibling classes (Location vs. Network vs. Junction).
3. **Walk the parent chain.** The right parent is the **most specific** class
   whose definition still covers your concept. Don't attach everything to
   `Component`.
4. **If nothing fits**, create an extension class under the closest parent —
   and give it the same annotations (see below), so the *next* mapping over
   your extension works too.
5. **Confirm consequential choices with the usecase author** — parent class,
   attribute kind, units, links. Propose your reasoning, get sign-off, then
   commit (this is the platform's "confirm, don't guess" rule).

### Decision tree for the top split

- Is it primarily **a place / spatial container** (things are *in* or *at* it)?
  → `Location` (a WindPark, a campus, a district).
- Is it **connective infrastructure** flows move through? → `Network`.
- Does it **transform energy or material**? → `Converter` (equipment) /
  `ConversionProcess` (the activity). Rotating fluid machines → `Turbine`.
- Does it **hold energy/material over time**? → `Storage`.
- Does it **produce** energy into the system? → `EnergyGenerator`.
  Does it **consume** it? → `EnergyConsumer`.
- Is it the **commodity carrying energy** (electricity, heat, gas)? → `EnergyCarrier`.
- Is it **something moving** between components? → `Flow`.
- Is it a **primary natural source** (wind, sun, coal seam)? → `Resource`.
- Does it **measure/control** (sensor, meter, controller, switch)? → `Device`.
- Is it a **person/organisation** owning or operating things? → `Actor`.
- Is it a **measurable property of a component** rather than a thing?
  → it's an `Attribute`, not a Component. Pick the kind:
  numeric+unit → `PhysicalAttribute`; enumerated → `CategoricalAttribute`;
  time-varying → `DynamicAttribute`; x-y curve → `CurveAttribute`;
  coordinates → `GeospatialAttribute`; money → `SimpleCostAttribute` /
  `UnitBasedCostAttribute`.

## Worked example: onboarding a wind forecasting usecase

Domain concepts: *wind park*, *wind turbine*, *wind speed forecast*,
*forecasted power output*.

| Concept | Wrong instinct | Correct mapping | Why |
|---|---|---|---|
| `WindPark` | subclass of `Wind` or `EnergyGenerator` | **`Location`** | It's a *site* — `Location` lists "Site"/"Area" as altLabels and "a wind park" as an example. The park *contains* turbines (`hasPart`/`locatedAt`). |
| `WindTurbine` | subclass of `Wind` | **`Turbine`** (under `EnergyConverter`) | The machine, not the resource. `Turbine`'s scope note says exactly this. |
| Wind speed | a plain number | **`DynamicAttribute`** on the park/turbine | Time-varying; the forecast series attaches via `hasFutureTimeSeries` → `FutureTimeSeries` (altLabels: "Forecast", "Prediction"). |
| The wind itself | — | **`Wind`** (a `RenewableResource`) | Only if the model reasons about the resource; see `Wind`'s scope note. |

Extension shape (each new term annotated so the next agent can map onto it):

```turtle
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

dici_onto:WindPark a owl:Class ;
    rdfs:subClassOf dici_onto:Location ;
    rdfs:label "Wind Park" ;
    rdfs:comment "A site grouping wind turbines and their shared infrastructure"@en ;
    skos:altLabel "Wind Farm"@en ;
    skos:example "An onshore wind park with 12 turbines and a grid connection point"@en .
```

## Rules that keep this working

- **Extensions must annotate too.** `tools/validate_extension.py` fails on a
  missing `rdfs:comment` and warns on missing `skos:definition` / `altLabel`
  / `example`. Terms cannot be promoted to core without the full set
  ([`CORE_EVOLUTION.md`](CORE_EVOLUTION.md)).
- **The TTL is the source of truth.** `term-index.json` / `term-index.md` are
  generated; never edit them by hand. CI fails if they're stale.
- **Query semantically.** Resolve types via `rdfs:subClassOf*` /
  `rdfs:subPropertyOf*`; never string-match class-name suffixes.
