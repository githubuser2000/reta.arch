# Architecture Status – current worked-through checklist

Date: 2026-04-23

This document condenses the distributed Stage/Audit history into one current status.
It does **not** repeat the old plan verbatim; it reclassifies items into:

- actually still open in code,
- effectively done but still present as compatibility facades,
- metadata/documentation lag.

## Current mathematical architecture

The following layers are present and active in the codebase:

- topology: `reta_architecture/topology.py`
- presheaves: `reta_architecture/presheaves.py`
- sheaves: `reta_architecture/sheaves.py`
- morphisms: `reta_architecture/morphisms.py`
- universal/gluing layer: `reta_architecture/universal.py`, `table_generation.py`, `program_workflow.py`
- category/functor/natural transformation layer: `reta_architecture/category_theory.py`
- meta-control: `architecture_map.py`, `architecture_contracts.py`, `architecture_witnesses.py`, `architecture_validation.py`, `architecture_coherence.py`, `architecture_impact.py`, `architecture_migration.py`, `architecture_rehearsal.py`, `architecture_activation.py`

Quantitative snapshot:

- 22 categories
- 62 functors
- 29 natural transformations
- 11 capsules
- 53 functorial routes
- 51/51 architecture validation checks passed
- coherence status: passed

## 1. Legacy owners – worked through

### `libs/center.py` — still a real remaining owner

Status: **open / highest priority**

Why:

- Stage 37 moved row-range logic into `reta_architecture/row_ranges.py`.
- Stage 38 moved arithmetic helpers into `reta_architecture/arithmetic.py`.
- Stage 39 moved console/help/utility logic into `reta_architecture/console_io.py`.
- `center.py` now delegates many functions, but it still acts as a kitchen-sink compatibility owner:
  - i18n proxy bootstrapping
  - global debug/output state
  - enum/export surface
  - several compatibility wrappers gathered in one place

Verdict:

`center.py` is no longer the algorithmic owner of the extracted domains, but it is still the thickest remaining compatibility surface.

Next move:

- isolate `nPmEnum` and remaining global state into explicit architecture/runtime modules
- reduce `center.py` to re-exports plus minimal compatibility glue
- keep public names stable

### `libs/lib4tables_prepare.py` — mostly migrated, but state ownership remains

Status: **partially open / second priority**

Why:

The module already delegates most operational work to:

- `reta_architecture.table_preparation`
- `reta_architecture.row_filtering`
- `reta_architecture.table_wrapping`

The remaining ownership is mainly:

- `Prepare.__init__` state shape
- wrapping/runtime synchronisation globals
- some legacy property surface

Verdict:

This is no longer a core algorithm owner. It is mainly a stateful façade around architecture-owned table preparation.

Next move:

- move remaining constructor/state conventions into `table_state.py` / `table_preparation.py` / `table_wrapping.py`
- leave `Prepare` as a minimal adapter class

### `libs/lib4tables_concat.py` — close to finished

Status: **largely done / low-to-medium priority**

Why:

The class methods already delegate almost entirely to:

- `reta_architecture.generated_columns`
- `reta_architecture.meta_columns`
- `reta_architecture.concat_csv`

The remaining legacy ownership is mostly:

- `Concat.__init__` state containers
- broad historical import surface

Verdict:

This file is much closer to a finished façade than the old inventory suggested.

Next move:

- move constructor state shape into an architecture bundle or explicit state object
- then reduce `Concat` to a thin compatibility adapter

### `reta.py` — effectively already a façade

Status: **mostly done / low priority**

Why:

`Program` delegates to:

- `RetaArchitecture.bootstrap(...)`
- `parameter_runtime`
- `program_workflow`
- architecture renderers and semantics builders

Verdict:

This is already a compatibility/program shell, not the main workflow owner.

Next move:

- optional cleanup only
- keep legacy `Program` API stable

### `retaPrompt.py` — effectively already a façade

Status: **mostly done / low priority**

Why:

The module is mostly wiring around:

- `PromptInteractionBundle`
- prompt preparation / execution / session bundles
- legacy function names forwarded to architecture-owned controller logic

Verdict:

Not a real algorithmic blocker anymore.

Next move:

- optional lazy bootstrap cleanup
- keep historical launcher/import surface intact

### `libs/LibRetaPrompt.py` — effectively already done

Status: **mostly done / very low priority**

Why:

The file contains import-time bootstrap/re-export wiring for:

- prompt runtime
- completion runtime
- prompt language
- prompt session

Verdict:

This is already an architecture bootstrap façade.

Next move:

- optional lazy-loading cleanup only

### Already thin enough

These items should no longer be treated as major open migration targets:

- `i18n/words.py`
- `libs/word_completerAlx.py`
- `libs/nestedAlx.py`
- `libs/lib4tables.py`
- `libs/tableHandling.py`

## 2. Migration waves – worked through

The important distinction is between **runtime reality** and **migration metadata**.

Runtime reality:

- Stages 37–41 are real activations, not just plans.
- Several old owners are already thin compatibility façades.

Migration metadata reality:

- `architecture_migration.py` still reports all waves as `ready_planned`.
- all steps still report `planned_not_executed`.

So the remaining work here is partly **code**, but also clearly **metadata lag**.

### M1 — Topology / presheaf data wave

Status: **mostly done in code, still open in documentation/data organization**

What is done:

- `i18n/words.py` is already a split compatibility façade
- topology/presheaf/sheaf layers exist

What remains:

- CSV/doc layer is still distributed rather than centrally described
- no single current status doc existed before this file

### M2 — Prompt / input morphism wave

Status: **substantially advanced, still partially open**

What is done:

- row ranges activated (Stage 37)
- arithmetic activated (Stage 38)
- console/help/utility activated (Stage 39)
- word completion activated (Stage 40)
- nested completion activated (Stage 41)

What remains:

- `center.py` is still the thick compatibility hub
- prompt wiring modules could be made lazier/thinner
- migration metadata still understates the achieved activation state

### M3 — Workflow / universal gluing wave

Status: **mostly done**

What is done:

- `reta.py` already delegates workflow logic into `program_workflow.py` and related architecture modules

What remains:

- mostly compatibility cleanup / reduction of residual shell code

### M4 — Table core / state wave

Status: **partially open**

What is done:

- many methods in `lib4tables_prepare.py` already delegate to architecture modules

What remains:

- constructor/state ownership and wrapping runtime state still sit in legacy surface

### M5 — Generated relation wave

Status: **largely done**

What is done:

- `lib4tables_concat.py` methods are already architecture-owned in practice

What remains:

- constructor/state container extraction
- reducing import surface

### M6 — Output / parity wave

Status: **code side mostly done, test-input side blocked**

What is done:

- `libs/lib4tables.py` is already a thin compatibility façade
- `libs/tableHandling.py` is already a thin compatibility façade

What remains:

- full parity run needs the missing reference archive

## 3. Parity test – worked through

Status: **blocked by missing reference artifact, not by a known code failure**

The parity test expects:

- `/mnt/data/reta.todel.zip`

Current outcome:

- the parity suite is skipped because the archive is absent

Interpretation:

- this is an environment/input gap
- it is not evidence of a regression in the new architecture by itself

Action required:

- provide the original archive in the expected location for full parity verification

## 4. Documentation – worked through

Status: **this was genuinely missing**

Before this file, the architecture history was spread across:

- Stage change logs
- architecture stage documents
- package audits
- markdown audits

This document is intended to serve as the single current status condensation.

## 5. Stronger runtime invariants – worked through

Status: **optional maturation step, not a current blocker**

This is a good next-phase quality task, but it should come after the remaining legacy-thinning work.

Recommended future additions:

- targeted property tests for naturality-sensitive routes
- stronger runtime assertions for selected commutative diagrams
- explicit invariants for key gluing paths and compatibility façades

## Actual priority order after working through the list

1. `libs/center.py`
2. `libs/lib4tables_prepare.py`
3. `libs/lib4tables_concat.py`
4. migration metadata refresh in `architecture_migration.py`
5. parity archive provisioning (`reta.todel.zip`)
6. optional lazy-cleanup in `reta.py`, `retaPrompt.py`, `libs/LibRetaPrompt.py`
7. stronger runtime invariants / property tests

## Bottom line

The old inventory slightly overstated how much is still open.

What is **really** still open in code:

- `center.py`
- residual state ownership in `lib4tables_prepare.py`
- residual constructor/state ownership in `lib4tables_concat.py`
- missing external reference archive for parity
- stale migration-status metadata

What is **not** really open anymore except as compatibility façades:

- `reta.py`
- `retaPrompt.py`
- `libs/LibRetaPrompt.py`
- `libs/lib4tables.py`
- `libs/tableHandling.py`
- `libs/word_completerAlx.py`
- `libs/nestedAlx.py`
- `i18n/words.py`
