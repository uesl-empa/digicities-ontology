# Linking to established domain ontologies

Digicities is a requirements-driven semantic layer that connects models to the
data they need: each model states its inputs as requirements against a shared
ontology, and the platform finds, checks and delivers that data from a
knowledge graph.

The core stays small on purpose. Detailed domains already have good
ontologies: Brick and BOT for buildings, IFC for building models, CityGML for
city models, CIM for power grids, OEO for energy system analysis, SAREF for
smart devices. This page explains how to link a Digicities class to a class in
one of those ontologies, and shows one checked example for each.

## The rule: link with SKOS, not with OWL equivalence

Use the SKOS mapping properties. The Digicities term is always the subject.

| Property | Use it when |
|---|---|
| `skos:exactMatch` | The two definitions are the same. |
| `skos:closeMatch` | Same concept, framed a little differently. |
| `skos:broadMatch` | The other class is **broader** than ours. |
| `skos:narrowMatch` | The other class is **narrower** than ours. |
| `skos:relatedMatch` | Same idea, but a different kind of thing (we model it as a component, they model it as a process or a data point). |

Do not use `owl:equivalentClass` or `rdfs:subClassOf` for these links unless
the definitions truly coincide. The platform runs a reasoner on every write.
An OWL link would let that reasoner change what our instances are. OEO, for
example, is built on BFO: declaring our `EnergyStorage` equal to an OEO class
would give every storage instance BFO's category commitments, which our model
does not make. A SKOS mapping states that two terms correspond. It has no
effect on reasoning. This follows the ontology's rule that a link never
changes what a thing is.

## Where mappings live today

Mappings are **not** in the core. The core v0.6.0 file contains no
`skos:*Match` statements. There are two places a mapping can live today.

1. **An alignment extension in a workspace.** A Turtle file of mapping
   statements in a workspace's `ontology/extensions/` folder. It is loaded into
   the workspace's ontology graph like any other extension, so you can query it.
   The `reference-ontologies` workspace holds two of these: `oeo_alignment.ttl`
   (the core's top-level classes against OEO) and `brick_alignment.ttl`
   (against Brick 1.4.4 and RealEstateCore). Every target IRI in those files was
   checked against the published ontology on 2026-08-19. Check a new file with
   `python tools/validate_extension.py <file>` before you add it.
2. **The Mapping view of the Ontology Manager.** Put the other ontology's Turtle
   file in `ontology/mappings/input/`, open **Ontology Manager**, choose the
   mapping input, then **Map Component** or **Map Attribute**. You pick one of
   `owl:equivalentClass`, `rdfs:subClassOf` or `skos:closeMatch`. The result is
   written to `ontology/mappings/output/<input>_2_dici_onto.ttl`.

Two limits of today's tooling:

- The Mapping view offers only one SKOS relation (`closeMatch`) and two OWL ones.
  For `exactMatch`, `broadMatch`, `narrowMatch` or `relatedMatch`, write an
  alignment extension.
- The Mapping view's output file is not loaded into the triplestore. Only
  `ontology/extensions/` is. The instruction file the ontology manager replays
  has no operation for mapping statements yet.

The planned alignment module (below) closes both gaps.

## Worked examples

One mapping per target ontology. The Digicities side is a core v0.6.0 class in
every example. The "Checked" column says how the target IRI was confirmed.

| Target | Mapping | Checked |
|---|---|---|
| OEO | `dici_onto:EnergyStorage skos:closeMatch oeo:OEO_00000159` ("energy storage object") | TIB Terminology Service, 2026-08-19 |
| OEO | `dici_onto:TimeSeries skos:exactMatch oeo:OEO_00030034` ("time series") | TIB Terminology Service, 2026-08-19 |
| Brick 1.4.4 | `dici_onto:Meter skos:closeMatch brick:Meter` | Brick 1.4.4 release file, 2026-08-19 |
| Brick 1.4.4 | `dici_onto:Sensor skos:relatedMatch brick:Sensor` | Brick 1.4.4 release file, 2026-08-19 |
| SAREF core 4.1.1 | `dici_onto:Device skos:closeMatch saref:Device` | `https://saref.etsi.org/core/` (v4.1.1), 2026-10-09 |
| SAREF4BLDG 2.1.1 | `dici_onto:EnergyConverter skos:closeMatch s4bldg:EnergyConversionDevice` | `https://saref.etsi.org/saref4bldg/` (v2.1.1), 2026-10-09 |
| SAREF4ENER 2.1.1 | `dici_onto:ElectricityDemandProfile skos:relatedMatch s4ener:PowerProfile` | `https://saref.etsi.org/saref4ener/` (v2.1.1), 2026-10-09 |
| BOT 0.3.2 | `dici_onto:Location skos:closeMatch bot:Zone` | `https://w3id.org/bot` (0.3.2), 2026-10-09 |
| ifcOWL (IFC4 ADD2 TC1) | `dici_onto:EnergyGenerator skos:narrowMatch ifc:IfcElectricGenerator` | TIB Terminology Service, 2026-10-09 |
| CIM (CGMES 3.0) | `dici_onto:EnergyStorage skos:narrowMatch cim:BatteryUnit` | ENTSO-E CGMES 3.0 Equipment RDFS (RDFS2020), 2026-10-09 |
| CityGML | none yet | see below |

Why each relation:

- **OEO.** OEO's "energy storage object" is an artificial object whose function
  is storing energy. Same concept, framed through BFO, so `closeMatch`. OEO's
  "time series" has the same definition as ours, so `exactMatch`.
- **Brick.** A Brick meter is the device, like ours. A Brick sensor is a
  *point*: a data channel on some equipment. Our `Sensor` is the hardware, and
  the data channel is an attribute on it. Same idea, different kind of thing,
  so `relatedMatch`.
- **SAREF core.** Both define a device as a physical thing built for a task.
- **SAREF4BLDG.** Its energy conversion device converts energy or transfers
  heat inside a building's distribution system. Ours converts energy anywhere.
  Close enough for `closeMatch`. For buildings themselves, our `Location` is
  broader, so `dici_onto:Location skos:narrowMatch s4bldg:Building` also holds.
- **SAREF4ENER.** A power profile is an object that exposes power sequences for
  flexibility. Our `ElectricityDemandProfile` is a time-series attribute. Same
  idea (power over time), different kind of thing, so `relatedMatch`.
- **BOT.** A BOT zone is any part of the world with a 3D extent; sites,
  buildings, storeys and spaces are zones. That matches our `Location`. A BOT
  building is narrower: `dici_onto:Location skos:narrowMatch bot:Building`.
- **ifcOWL.** IFC's electric generator produces electricity only. Our
  `EnergyGenerator` produces any form of energy, so theirs is narrower.
  buildingSMART itself advises linked-data users to look at bSDD rather than
  ifcOWL; the mapping pattern is the same for bSDD terms.
- **CIM.** CGMES's battery unit is an electrochemical storage device on the
  grid. Our `EnergyStorage` covers any stored energy, so theirs is narrower.
- **CityGML.** We did not find an official OWL version of CityGML 3.0 with
  stable class IRIs. The OGC standard is published as a conceptual model and a
  GML encoding. A 2024 research effort ("CityOWL", ISPRS Annals X-4-W4-2024)
  converts the model to OWL, but we have not checked its IRIs. Until there is
  a stable namespace, link CityGML data where you import it, not in the
  ontology.

Prefixes used above:

```turtle
@prefix dici_onto: <https://digicities.info/ontology#> .
@prefix skos:   <http://www.w3.org/2004/02/skos/core#> .
@prefix oeo:    <https://openenergyplatform.org/ontology/oeo/> .
@prefix brick:  <https://brickschema.org/schema/Brick#> .
@prefix saref:  <https://saref.etsi.org/core/> .
@prefix s4bldg: <https://saref.etsi.org/saref4bldg/> .
@prefix s4ener: <https://saref.etsi.org/saref4ener/> .
@prefix bot:    <https://w3id.org/bot#> .
@prefix ifc:    <https://standards.buildingsmart.org/IFC/DEV/IFC4/ADD2_TC1/OWL#> .
@prefix cim:    <http://iec.ch/TC57/CIM100#> .
```

## Writing an alignment extension

1. Make one Turtle file per target ontology, for example
   `ontology/extensions/saref_alignment.ttl`.
2. Declare no new classes in it. It only holds mapping statements whose
   subject is a Digicities term.
3. Above each mapping, quote the target term's label and definition and the
   date you checked it, as `oeo_alignment.ttl` does. Pin the target's version.
4. Check it: `python tools/validate_extension.py ontology/extensions/saref_alignment.ttl`.
   A file of mappings only passes with a warning that it declares no classes.
5. Load it into the graph with the **Provision graph** button in the web app's
   workspace header (or rebuild the workspace). The mappings then sit in the
   ontology graph.

To list the mappings of a workspace:

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT ?ours ?relation ?theirs
FROM <http://ontology_dici_onto>
WHERE {
  VALUES ?relation { skos:exactMatch skos:closeMatch skos:broadMatch
                     skos:narrowMatch skos:relatedMatch }
  ?ours ?relation ?theirs .
}
```

## Planned: alignment module (not implemented)

This is planned and does not exist yet.

- One alignment file per target ontology, released with the core, with the
  target version pinned and every IRI checked by a test against the published
  release.
- An ontology manager operation for mapping statements, so alignments are made
  and replayed through the same tooling as everything else, with all five SKOS
  relations.
- Constraints written as SHACL shapes in a separate file, so that data
  exchanged with those ontologies can be validated without changing the core.

Until then, alignment extensions in a workspace (above) are the way to link.
