from __future__ import annotations

"""Stage-29 commutative architecture contracts for the Reta refactor.

Stage 27 names categories, functors and natural transformations.  Stage 28 draws
Reta as a capsule map.  Stage 29 makes the important naturality/parity claims
explicit as commutative diagrams, capsule boundary contracts and refactor laws.

This module is deliberately metadata-only.  It validates references against the
existing category-theory and architecture-map bundles, but it does not execute or
change the CLI/table runtime.
"""

from dataclasses import dataclass
from typing import Mapping, Sequence


@dataclass(frozen=True)
class DiagramArrowSpec:
    """One symbolic arrow in a commutative architecture diagram."""

    source: str
    target: str
    label: str
    code_owner: str
    paradigm_terms: Sequence[str]

    def snapshot(self) -> dict:
        return {
            "source": self.source,
            "target": self.target,
            "label": self.label,
            "code_owner": self.code_owner,
            "paradigm_terms": list(self.paradigm_terms),
        }


@dataclass(frozen=True)
class CommutativeDiagramSpec:
    """A named diagram whose top and bottom paths must agree semantically."""

    name: str
    diagram_type: str
    nodes: Mapping[str, str]
    top_path: Sequence[DiagramArrowSpec]
    bottom_path: Sequence[DiagramArrowSpec]
    equality: str
    capsules: Sequence[str]
    categories: Sequence[str]
    functors: Sequence[str]
    natural_transformations: Sequence[str]
    verification: Sequence[str]
    stage_origin: str
    description: str

    def snapshot(self) -> dict:
        return {
            "name": self.name,
            "diagram_type": self.diagram_type,
            "nodes": dict(self.nodes),
            "top_path": [item.snapshot() for item in self.top_path],
            "bottom_path": [item.snapshot() for item in self.bottom_path],
            "equality": self.equality,
            "capsules": list(self.capsules),
            "categories": list(self.categories),
            "functors": list(self.functors),
            "natural_transformations": list(self.natural_transformations),
            "verification": list(self.verification),
            "stage_origin": self.stage_origin,
            "description": self.description,
        }


@dataclass(frozen=True)
class CapsuleContractSpec:
    """Boundary contract for one Stage-28/29 architecture capsule."""

    capsule: str
    owns: Sequence[str]
    accepts: Sequence[str]
    produces: Sequence[str]
    must_not_own: Sequence[str]
    primary_category: str
    primary_functor_or_transformation: str
    protected_by: Sequence[str]
    implementation_anchors: Sequence[str]
    stage_span: str
    description: str

    def snapshot(self) -> dict:
        return {
            "capsule": self.capsule,
            "owns": list(self.owns),
            "accepts": list(self.accepts),
            "produces": list(self.produces),
            "must_not_own": list(self.must_not_own),
            "primary_category": self.primary_category,
            "primary_functor_or_transformation": self.primary_functor_or_transformation,
            "protected_by": list(self.protected_by),
            "implementation_anchors": list(self.implementation_anchors),
            "stage_span": self.stage_span,
            "description": self.description,
        }


@dataclass(frozen=True)
class RefactorLawSpec:
    """A human-readable invariant that future stages should preserve."""

    name: str
    law_type: str
    applies_to: Sequence[str]
    mathematical_reading: str
    reta_reading: str
    protected_paths: Sequence[str]
    evidence: Sequence[str]
    status: str

    def snapshot(self) -> dict:
        return {
            "name": self.name,
            "law_type": self.law_type,
            "applies_to": list(self.applies_to),
            "mathematical_reading": self.mathematical_reading,
            "reta_reading": self.reta_reading,
            "protected_paths": list(self.protected_paths),
            "evidence": list(self.evidence),
            "status": self.status,
        }


@dataclass(frozen=True)
class ContractValidationSpec:
    """Reference validation against CategoryTheoryBundle and ArchitectureMapBundle."""

    status: str
    known_capsules: Sequence[str]
    known_categories: Sequence[str]
    known_functors: Sequence[str]
    known_natural_transformations: Sequence[str]
    missing_capsules: Sequence[str]
    missing_categories: Sequence[str]
    missing_functors: Sequence[str]
    missing_natural_transformations: Sequence[str]

    def snapshot(self) -> dict:
        return {
            "status": self.status,
            "known_capsules": list(self.known_capsules),
            "known_categories": list(self.known_categories),
            "known_functors": list(self.known_functors),
            "known_natural_transformations": list(self.known_natural_transformations),
            "missing_capsules": list(self.missing_capsules),
            "missing_categories": list(self.missing_categories),
            "missing_functors": list(self.missing_functors),
            "missing_natural_transformations": list(self.missing_natural_transformations),
        }


@dataclass(frozen=True)
class Stage29ArchitecturePlan:
    """Bridge from Stage 28's map to Stage 29's contracts."""

    planned_after_stage_28: Sequence[str]
    implemented_in_stage_29: Sequence[str]
    inherited_from_previous_stages: Sequence[str]
    behaviour_change: str

    def snapshot(self) -> dict:
        return {
            "planned_after_stage_28": list(self.planned_after_stage_28),
            "implemented_in_stage_29": list(self.implemented_in_stage_29),
            "inherited_from_previous_stages": list(self.inherited_from_previous_stages),
            "behaviour_change": self.behaviour_change,
        }


@dataclass(frozen=True)
class ArchitectureContractsBundle:
    """Inspectable Stage-29 contracts over the categorical architecture."""

    diagrams: Sequence[CommutativeDiagramSpec]
    capsule_contracts: Sequence[CapsuleContractSpec]
    laws: Sequence[RefactorLawSpec]
    mermaid_diagram: str
    text_diagram: str
    validation: ContractValidationSpec
    plan: Stage29ArchitecturePlan

    def diagram_named(self, name: str) -> CommutativeDiagramSpec:
        for diagram in self.diagrams:
            if diagram.name == name:
                return diagram
        raise KeyError(f"Unknown commutative diagram: {name}")

    def capsule_contract_named(self, capsule: str) -> CapsuleContractSpec:
        for contract in self.capsule_contracts:
            if contract.capsule == capsule:
                return contract
        raise KeyError(f"Unknown capsule contract: {capsule}")

    def snapshot(self) -> dict:
        return {
            "class": type(self).__name__,
            "stage": 29,
            "purpose": "Kommutierende Architekturverträge, Kapselgrenzen und Refactor-Gesetze für das Topologie-/Garben-/Kategorien-Paradigma.",
            "paradigm": [
                "topology",
                "morphism",
                "universal_property",
                "presheaf",
                "sheaf",
                "category",
                "functor",
                "natural_transformation",
                "commutative_diagram",
                "capsule_contract",
            ],
            "counts": {
                "commutative_diagrams": len(self.diagrams),
                "capsule_contracts": len(self.capsule_contracts),
                "laws": len(self.laws),
            },
            "validation": self.validation.snapshot(),
            "commutative_diagrams": [item.snapshot() for item in self.diagrams],
            "capsule_contracts": [item.snapshot() for item in self.capsule_contracts],
            "laws": [item.snapshot() for item in self.laws],
            "diagrams": {
                "text": self.text_diagram,
                "mermaid": self.mermaid_diagram,
            },
            "plan": self.plan.snapshot(),
        }


def _arrow(source: str, target: str, label: str, code_owner: str, paradigm_terms: Sequence[str]) -> DiagramArrowSpec:
    return DiagramArrowSpec(source, target, label, code_owner, tuple(paradigm_terms))


def _diagram(
    name: str,
    diagram_type: str,
    nodes: Mapping[str, str],
    top_path: Sequence[DiagramArrowSpec],
    bottom_path: Sequence[DiagramArrowSpec],
    equality: str,
    capsules: Sequence[str],
    categories: Sequence[str],
    functors: Sequence[str],
    natural_transformations: Sequence[str],
    verification: Sequence[str],
    description: str,
) -> CommutativeDiagramSpec:
    return CommutativeDiagramSpec(
        name=name,
        diagram_type=diagram_type,
        nodes=dict(nodes),
        top_path=tuple(top_path),
        bottom_path=tuple(bottom_path),
        equality=equality,
        capsules=tuple(capsules),
        categories=tuple(categories),
        functors=tuple(functors),
        natural_transformations=tuple(natural_transformations),
        verification=tuple(verification),
        stage_origin="Stage 29",
        description=description,
    )


def _diagrams() -> tuple[CommutativeDiagramSpec, ...]:
    return (
        _diagram(
            "RawCommandNaturalitySquare",
            "naturality square",
            {"A": "Raw command over U", "B": "Raw command over V", "C": "Canonical parameters over U", "D": "Canonical parameters over V"},
            (
                _arrow("A", "B", "restrict U→V", "topology.py + presheaves.py", ("topology", "presheaf", "morphism")),
                _arrow("B", "D", "canonicalize raw tokens", "prompt_language.py + sheaves.py", ("morphism", "sheaf")),
            ),
            (
                _arrow("A", "C", "canonicalize raw tokens", "input_semantics.py + prompt_runtime.py", ("functor", "natural_transformation")),
                _arrow("C", "D", "restrict canonical section", "topology.py + sheaves.py", ("topology", "sheaf")),
            ),
            "canonicalize(restrict(raw,U→V)) = restrict(canonicalize(raw),U→V)",
            ("InputPromptCapsule", "SemanticSheafCapsule"),
            ("OpenRetaContextCategory", "CanonicalSemanticSheafCategory"),
            ("RawCommandPresheafFunctor", "CanonicalParameterSheafFunctor"),
            ("RawToCanonicalParameterTransformation",),
            ("known alias lookup", "prompt-language regression tests"),
            "Raw CLI/prompt text remains compatible with context restriction and canonical parameter semantics.",
        ),
        _diagram(
            "PresheafSheafGluingSquare",
            "sheafification square",
            {"A": "Local sections over cover(U)", "B": "Local sections over cover(V)", "C": "Sheaf section over U", "D": "Sheaf section over V"},
            (
                _arrow("A", "B", "restrict local sections", "presheaves.py", ("presheaf", "morphism")),
                _arrow("B", "D", "glue compatible sections", "sheaves.py + universal.py", ("sheaf", "universal_property")),
            ),
            (
                _arrow("A", "C", "glue compatible sections", "sheaves.py + semantics_builder.py", ("sheaf", "universal_property")),
                _arrow("C", "D", "restrict glued section", "topology.py + sheaves.py", ("topology", "morphism")),
            ),
            "glue(restrict(local_sections,V)) = restrict(glue(local_sections),V)",
            ("LocalSectionCapsule", "SemanticSheafCapsule"),
            ("LocalSectionCategory", "CanonicalSemanticSheafCategory"),
            ("LocalDataPresheafFunctor", "GluedSemanticSheafFunctor"),
            ("PresheafToSheafGluingTransformation",),
            ("presheaves-json", "sheaves-json", "semantic count regressions"),
            "CSV, translation and prompt sections are local data that glue into one semantic sheaf without changing meaning under restriction.",
        ),
        _diagram(
            "UniversalWorkflowTableSquare",
            "universal construction square",
            {"A": "Canonical semantics", "B": "Workflow gluing input", "C": "Legacy Program table view", "D": "Global table section"},
            (
                _arrow("A", "B", "parameter runtime + column selection", "parameter_runtime.py + column_selection.py", ("functor", "morphism")),
                _arrow("B", "D", "universal table generation", "table_generation.py + universal.py", ("universal_property", "sheaf")),
            ),
            (
                _arrow("A", "C", "legacy Program facade", "reta.py", ("morphism", "legacy")),
                _arrow("C", "D", "architecture sync", "facade.py + program_workflow.py", ("natural_transformation", "morphism")),
            ),
            "architecture_table(canonical_semantics) = sync(legacy_program(canonical_semantics))",
            ("WorkflowGluingCapsule", "TableCoreCapsule", "CompatibilityCapsule"),
            ("CanonicalSemanticSheafCategory", "UniversalConstructionCategory", "TableSectionCategory"),
            ("TableGenerationGluingFunctor", "ArchitectureRuntimeFunctor"),
            ("TableGenerationGluingTransformation", "LegacyToArchitectureTransformation"),
            ("program workflow tests", "command parity tests"),
            "The global table is constructed at the universal workflow node, not by hidden ownership in reta.py.",
        ),
        _diagram(
            "GeneratedColumnStateSyncSquare",
            "endomorphism/state square",
            {"A": "Table section", "B": "Generated/enriched table", "C": "Explicit TableStateSections", "D": "Generated-column state"},
            (
                _arrow("A", "B", "generated-column endofunctor", "generated_columns.py", ("functor", "morphism")),
                _arrow("B", "D", "project generated state", "table_runtime.py + table_state.py", ("natural_transformation", "sheaf")),
            ),
            (
                _arrow("A", "C", "project explicit state", "table_state.py", ("morphism", "sheaf")),
                _arrow("C", "D", "sync generated metadata", "sheaves.py + universal.py", ("natural_transformation", "universal_property")),
            ),
            "project_state(Gᵢ(table)) = sync_generated(project_state(table))",
            ("GeneratedRelationCapsule", "TableCoreCapsule"),
            ("GeneratedColumnEndomorphismCategory", "TableSectionCategory"),
            ("GeneratedColumnEndofunctorFamily", "ExplicitTableStateFunctor"),
            ("GeneratedColumnsSheafSyncTransformation", "TableRuntimeToStateSectionsTransformation"),
            ("table_state tests", "generated_columns tests"),
            "Generated-column effects must be visible in table content, sheaf metadata and explicit table state together.",
        ),
        _diagram(
            "RuntimeStateProjectionSquare",
            "projection square",
            {"A": "Mutable Tables runtime", "B": "Mutated Tables runtime", "C": "TableStateSections", "D": "tableStateSnapshot"},
            (
                _arrow("A", "B", "legacy attribute mutation", "table_runtime.py", ("morphism", "legacy")),
                _arrow("B", "D", "snapshot", "table_runtime.py + table_state.py", ("natural_transformation", "sheaf")),
            ),
            (
                _arrow("A", "C", "route through state sections", "table_state.py", ("morphism", "sheaf")),
                _arrow("C", "D", "snapshot", "table_state.py", ("natural_transformation",)),
            ),
            "snapshot(mutate_legacy(Tables)) = snapshot(update_state_sections(Tables))",
            ("TableCoreCapsule",),
            ("TableSectionCategory",),
            ("MutableTableRuntimeFunctor", "ExplicitTableStateFunctor"),
            ("TableRuntimeToStateSectionsTransformation",),
            ("table_state snapshot tests",),
            "The mutable legacy-compatible Tables object and explicit state sections must show the same state.",
        ),
        _diagram(
            "RenderedOutputParitySquare",
            "output parity square",
            {"A": "Prepared table", "B": "Architecture rendered output", "C": "Legacy rendered output", "D": "Normalized comparable output"},
            (
                _arrow("A", "B", "architecture renderer", "table_output.py + output_syntax.py", ("functor", "morphism")),
                _arrow("B", "D", "normalize", "tests/test_command_parity.py", ("natural_transformation",)),
            ),
            (
                _arrow("A", "C", "legacy renderer", "libs/tableHandling.py + libs/lib4tables.py", ("legacy", "morphism")),
                _arrow("C", "D", "normalize", "tests/test_command_parity.py", ("natural_transformation",)),
            ),
            "normalize(render_arch(table)) = normalize(render_legacy(table))",
            ("OutputRenderingCapsule", "CompatibilityCapsule"),
            ("TableSectionCategory", "OutputFormatCategory", "LegacyFacadeCategory"),
            ("OutputRenderingFunctorFamily", "NormalizedOutputFunctor", "LegacyRuntimeFunctor"),
            ("RenderedOutputNormalizationTransformation", "LegacyToArchitectureTransformation"),
            ("Shell/Markdown/HTML parity", "gebrochenuniversum parity"),
            "Renderer-internal paths may differ, but normalized observable output must remain compatible.",
        ),
        _diagram(
            "LegacyArchitectureCompatibilitySquare",
            "compatibility square",
            {"A": "Legacy command/import", "B": "Legacy observable result", "C": "Architecture observable result", "D": "Same observable result"},
            (
                _arrow("A", "B", "old facade path", "reta.py + retaPrompt.py + libs", ("legacy", "morphism")),
                _arrow("B", "D", "parity comparison", "tests/test_command_parity.py", ("natural_transformation",)),
            ),
            (
                _arrow("A", "C", "architecture facade path", "facade.py", ("functor", "natural_transformation")),
                _arrow("C", "D", "parity comparison", "tests/test_command_parity.py", ("natural_transformation",)),
            ),
            "observe(legacy(command)) = observe(architecture(command))",
            ("CompatibilityCapsule", "RetaArchitectureRoot"),
            ("LegacyFacadeCategory", "OutputFormatCategory"),
            ("LegacyRuntimeFunctor", "ArchitectureRuntimeFunctor", "NormalizedOutputFunctor"),
            ("LegacyToArchitectureTransformation",),
            ("package integrity", "command parity"),
            "Legacy surfaces are façades into the architecture, not an independent second owner of semantics.",
        ),
        _diagram(
            "ArchitectureMapContractReflectionTriangle",
            "reflection triangle",
            {"A": "CategoryTheoryBundle", "B": "ArchitectureMapBundle", "C": "ArchitectureContractsBundle", "D": "Validated contracts"},
            (
                _arrow("A", "C", "CategoryTheoryToContractFunctor", "category_theory.py + architecture_contracts.py", ("category", "functor")),
                _arrow("C", "D", "ContractReferenceValidation", "architecture_contracts.py", ("morphism", "universal_property")),
            ),
            (
                _arrow("B", "C", "ArchitectureMapToContractFunctor", "architecture_map.py + architecture_contracts.py", ("functor", "natural_transformation")),
                _arrow("C", "D", "ContractReferenceValidation", "architecture_contracts.py", ("morphism", "universal_property")),
            ),
            "validate(contracts(category_theory)) = validate(contracts(architecture_map))",
            ("CategoricalMetaCapsule",),
            ("CommutativeArchitectureContractCategory",),
            ("CategoryTheoryToContractFunctor", "ArchitectureMapToContractFunctor"),
            ("ContractedNaturalityTransformation",),
            ("architecture-contracts-json validation",),
            "The Stage-29 contract layer itself is a reflected view of the category bundle and the capsule map.",
        ),
    )


def _contract(
    capsule: str,
    owns: Sequence[str],
    accepts: Sequence[str],
    produces: Sequence[str],
    must_not_own: Sequence[str],
    primary_category: str,
    primary_functor_or_transformation: str,
    protected_by: Sequence[str],
    implementation_anchors: Sequence[str],
    stage_span: str,
    description: str,
) -> CapsuleContractSpec:
    return CapsuleContractSpec(
        capsule=capsule,
        owns=tuple(owns),
        accepts=tuple(accepts),
        produces=tuple(produces),
        must_not_own=tuple(must_not_own),
        primary_category=primary_category,
        primary_functor_or_transformation=primary_functor_or_transformation,
        protected_by=tuple(protected_by),
        implementation_anchors=tuple(implementation_anchors),
        stage_span=stage_span,
        description=description,
    )


def _capsule_contracts() -> tuple[CapsuleContractSpec, ...]:
    return (
        _contract("RetaArchitectureRoot", ("bootstrap order", "architecture facade"), ("legacy entry points",), ("snapshots", "bundle access"), ("domain-specific generated-column semantics",), "UniversalConstructionCategory", "ArchitectureRuntimeFunctor", ("snapshot-json",), ("facade.py", "__init__.py"), "Stages 1-29", "Root coordinates bundles without owning their inner semantics."),
        _contract("SchemaTopologyCapsule", ("schema", "open contexts", "basis covers"), ("i18n split modules", "tags"), ("ContextSelection", "RetaContextTopology"), ("table output rendering",), "OpenRetaContextCategory", "SchemaToTopologyFunctor", ("topology-json",), ("schema.py", "topology.py", "split_i18n.py"), "Stages 1-4", "Owns the topology base over reta contexts."),
        _contract("LocalSectionCapsule", ("local CSV/doc/prompt sections", "restriction maps"), ("filesystem", "open contexts"), ("restricted local sections",), ("canonical global semantics",), "LocalSectionCategory", "LocalDataPresheafFunctor", ("presheaves-json",), ("presheaves.py",), "Stage 1 onward", "Owns presheaf-like local data, not the glued sheaf meaning."),
        _contract("SemanticSheafCapsule", ("canonical parameter semantics", "generated/output/html sheaves"), ("local sections", "schema"), ("canonical pairs", "column numbers"), ("CLI parsing", "renderer syntax"), "CanonicalSemanticSheafCategory", "PresheafToSheafGluingTransformation", ("sheaves-json", "known pair lookup"), ("sheaves.py", "semantics_builder.py"), "Stages 1-3, 27-29", "Owns glued global semantic meaning."),
        _contract("InputPromptCapsule", ("prompt/runtime/completion/session/execution/preparation/interaction"), ("raw CLI/prompt text",), ("canonical command tokens", "prompt calls"), ("table rendering", "generated-column algorithms"), "OpenRetaContextCategory", "RawCommandPresheafFunctor", ("prompt-* tests",), ("input_semantics.py", "prompt_*.py"), "Stages 4, 6-12", "Owns raw input and prompt morphisms."),
        _contract("WorkflowGluingCapsule", ("parameter runtime", "column selection", "program workflow", "table generation gluing"), ("canonical semantics", "CLI args"), ("workflow result", "table-generation input"), ("mutable table internals",), "UniversalConstructionCategory", "TableGenerationGluingTransformation", ("program-workflow-json",), ("parameter_runtime.py", "column_selection.py", "program_workflow.py", "table_generation.py"), "Stages 13-15", "Owns the universal construction from semantics to table-generation input."),
        _contract("TableCoreCapsule", ("global table section", "explicit table state", "prepare/row/wrapping/number morphisms"), ("workflow result", "generated effects"), ("prepared table", "TableStateSections"), ("output syntax ownership", "CSV source ownership"), "TableSectionCategory", "TableRuntimeToStateSectionsTransformation", ("table-state-json", "table-runtime-json"), ("table_runtime.py", "table_state.py", "table_preparation.py", "row_filtering.py", "table_wrapping.py", "number_theory.py"), "Stages 16, 22-26", "Owns table state and preparation as explicit sections and morphisms."),
        _contract("GeneratedRelationCapsule", ("generated columns", "meta columns", "concat CSV", "combi join"), ("table section", "local CSV sections"), ("enriched table", "generated state"), ("renderer normalization",), "GeneratedColumnEndomorphismCategory", "GeneratedColumnEndofunctorFamily", ("generated-columns-json", "concat-csv-json", "combi-join-json"), ("generated_columns.py", "meta_columns.py", "concat_csv.py", "combi_join.py"), "Stages 17-19, 21", "Owns relation/enrichment morphisms on table sections."),
        _contract("OutputRenderingCapsule", ("output syntax", "output semantics", "table output renderers"), ("prepared table", "output mode"), ("rendered output",), ("legacy parity comparison",), "OutputFormatCategory", "OutputRenderingFunctorFamily", ("output-syntax-json", "table-output-json"), ("output_syntax.py", "output_semantics.py", "table_output.py"), "Stages 5, 20, 24", "Owns renderer functors from table sections to output formats."),
        _contract("CompatibilityCapsule", ("legacy facades", "package integrity", "command parity"), ("old command/import paths", "original archive"), ("same observable output", "manifest"), ("new canonical semantic ownership",), "LegacyFacadeCategory", "LegacyToArchitectureTransformation", ("package-integrity-json", "tests/test_command_parity.py"), ("reta.py", "retaPrompt.py", "libs/*", "package_integrity.py"), "Stages 3-29", "Owns compatibility surfaces and parity checks, not domain semantics."),
        _contract("CategoricalMetaCapsule", ("category theory", "architecture map", "architecture contracts"), ("all bundle metadata",), ("category-theory-json", "architecture-map-json", "architecture-contracts-json"), ("runtime domain mutation",), "CommutativeArchitectureContractCategory", "ContractedNaturalityTransformation", ("architecture-contracts-json validation",), ("category_theory.py", "architecture_map.py", "architecture_contracts.py"), "Stages 27-29", "Owns the symbolic categorical map, diagrams, contracts and validation."),
    )


def _law(name: str, law_type: str, applies_to: Sequence[str], mathematical_reading: str, reta_reading: str, protected_paths: Sequence[str], evidence: Sequence[str]) -> RefactorLawSpec:
    return RefactorLawSpec(name, law_type, tuple(applies_to), mathematical_reading, reta_reading, tuple(protected_paths), tuple(evidence), "documented and reference-validated in Stage 29")


def _laws() -> tuple[RefactorLawSpec, ...]:
    return (
        _law("ContextRefinementCompositionLaw", "topology/category", ("SchemaTopologyCapsule", "OpenRetaContextCategory"), "Context refinements compose.", "Sprache/Parameter/Zeilen/Ausgabe-Kontexte dürfen bei kompatibler Verfeinerung nicht ordnungsabhängig werden.", ("ContextSelection.refine",), ("topology-json",)),
        _law("PresheafRestrictionLaw", "presheaf", ("LocalSectionCapsule", "LocalSectionCategory"), "Restrictions compose along W⊆V⊆U.", "Lokale CSV-/Prompt-Sektionen behalten bei mehrfacher Einschränkung dieselbe Bedeutung wie bei direkter Einschränkung.", ("Presheaf.restrict",), ("presheaves-json",)),
        _law("SheafGluingUniquenessLaw", "sheaf/universal", ("SemanticSheafCapsule", "UniversalConstructionCategory"), "Compatible local sections glue to a unique represented global section.", "Parametersemantik soll nur über den kanonischen Builder/Gluing-Knoten global werden.", ("SheafBundle", "UniversalBundle"), ("known pair lookup", "semantic regression counts")),
        _law("RawCanonicalNaturalityLaw", "natural transformation", ("InputPromptCapsule", "SemanticSheafCapsule"), "Raw-command functor to canonical-parameter functor is natural in context restriction.", "Aliasauflösung und Kontextverfeinerung dürfen sich nicht widersprechen.", ("RawToCanonicalParameterTransformation",), ("prompt language tests",)),
        _law("WorkflowUniversalConstructionLaw", "universal property", ("WorkflowGluingCapsule", "TableCoreCapsule"), "The workflow construction mediates from canonical semantics to table sections.", "Tabellenbau gehört in den Workflow-Gluing-Knoten, nicht zurück in reta.py als Monolith.", ("TableGenerationGluingTransformation",), ("program-workflow-json",)),
        _law("GeneratedColumnStateSyncLaw", "functor/natural transformation", ("GeneratedRelationCapsule", "TableCoreCapsule"), "Generated-column endofunctors commute with explicit state projection.", "Generierte Spalten müssen TableStateSections und Sheaf-Metadaten synchron halten.", ("GeneratedColumnsSheafSyncTransformation",), ("table_state tests",)),
        _law("RuntimeStateProjectionLaw", "projection", ("TableCoreCapsule",), "Mutable runtime projection and explicit state section update have the same snapshot.", "Legacy-Attribute an Tables bleiben kompatibel, aber der Zustand ist explizit gekapselt.", ("TableRuntimeToStateSectionsTransformation",), ("table-state-json",)),
        _law("OutputNormalizationNaturalityLaw", "natural transformation", ("OutputRenderingCapsule", "CompatibilityCapsule"), "Output normalization is natural over supported renderer paths.", "HTML/Markdown/Shell dürfen intern anders laufen, müssen aber normalisiert paritätsfähig bleiben.", ("RenderedOutputNormalizationTransformation",), ("command parity tests",)),
        _law("LegacyCompatibilityNaturalityLaw", "compatibility natural transformation", ("CompatibilityCapsule", "RetaArchitectureRoot"), "LegacyRuntimeFunctor naturally transforms into ArchitectureRuntimeFunctor on supported command/import contexts.", "Alte Startdateien und libs sind Fassaden; neue Semantik gehört den Architektur-Kapseln.", ("LegacyToArchitectureTransformation",), ("package integrity", "command parity tests")),
    )


_TEXT_DIAGRAM = """\
ArchitectureContractsBundle
├─ Commutative diagrams
│  ├─ RawCommandNaturalitySquare
│  ├─ PresheafSheafGluingSquare
│  ├─ UniversalWorkflowTableSquare
│  ├─ GeneratedColumnStateSyncSquare
│  ├─ RuntimeStateProjectionSquare
│  ├─ RenderedOutputParitySquare
│  ├─ LegacyArchitectureCompatibilitySquare
│  └─ ArchitectureMapContractReflectionTriangle
├─ Capsule contracts
│  ├─ RetaArchitectureRoot
│  ├─ SchemaTopologyCapsule
│  ├─ LocalSectionCapsule
│  ├─ SemanticSheafCapsule
│  ├─ InputPromptCapsule
│  ├─ WorkflowGluingCapsule
│  ├─ TableCoreCapsule
│  ├─ GeneratedRelationCapsule
│  ├─ OutputRenderingCapsule
│  ├─ CompatibilityCapsule
│  └─ CategoricalMetaCapsule
└─ Refactor laws
   ├─ topology / presheaf / sheaf laws
   ├─ universal workflow law
   ├─ generated/state sync law
   ├─ output-normalization law
   └─ legacy-compatibility law
"""


_MERMAID_DIAGRAM = """\
```mermaid
flowchart TD
    Raw[Raw CLI/Prompt] -->|RawCommandNaturalitySquare| Canonical[Canonical semantic sheaf]
    Local[Local CSV/doc/prompt sections] -->|PresheafSheafGluingSquare| Canonical
    Canonical -->|UniversalWorkflowTableSquare| Table[Global table section]
    Table -->|GeneratedColumnStateSyncSquare| Generated[Generated/enriched state]
    Table -->|RuntimeStateProjectionSquare| State[Explicit TableStateSections]
    Table -->|RenderedOutputParitySquare| Output[Normalized output]
    Legacy[Legacy reta.py/retaPrompt.py/libs] -->|LegacyArchitectureCompatibilitySquare| Output
    Meta[CategoryTheoryBundle + ArchitectureMapBundle] -->|ArchitectureMapContractReflectionTriangle| Contracts[ArchitectureContractsBundle]
    Contracts -->|ContractReferenceValidation| Validated[Validated Stage-29 contracts]
```
"""


def _plan() -> Stage29ArchitecturePlan:
    return Stage29ArchitecturePlan(
        planned_after_stage_28=(
            "Die Stage-28-Kapselkarte nicht nur zeichnen, sondern als kommutierende Pfade und prüfbare Architekturverträge festhalten.",
            "Natürliche Transformationen mit konkreten Top-/Bottom-Pfaden, Kapseln, Kategorien und Prüfankern verbinden.",
            "Für jede Kapsel definieren, was sie besitzt, was sie annimmt, was sie produziert und was sie ausdrücklich nicht besitzen soll.",
        ),
        implemented_in_stage_29=(
            "Neue Datei reta_architecture/architecture_contracts.py mit CommutativeDiagramSpec, CapsuleContractSpec, RefactorLawSpec und ArchitectureContractsBundle.",
            "Acht kommutierende Diagramme verbinden Topologie, Prägarben, Garben, universelles Gluing, Tabellenzustand, Renderer, Legacy-Parität und Meta-Validierung.",
            "Elf Kapselverträge legen stufenweise fest, welche reta-Teile in welcher Kapsel liegen und welche Grenzen nicht verletzt werden sollen.",
            "Neun Refactor-Gesetze formulieren die Architektur-Invarianten, die spätere Stages schützen müssen.",
            "Die Vertragsreferenzen werden gegen CategoryTheoryBundle und ArchitectureMapBundle validiert.",
        ),
        inherited_from_previous_stages=(
            "Stage 1-3: Topologie, Prägarben, Garben und i18n-/Schema-Split.",
            "Stage 4-12: Input-/Prompt-Kapseln.",
            "Stage 13-26: Workflow-Gluing, Tabellenkern, Generated/Output/State-Schichten.",
            "Stage 27: Kategorien, Funktoren und natürliche Transformationen.",
            "Stage 28: Gesamtarchitekturkarte und Kapselbaum.",
        ),
        behaviour_change="keine beabsichtigte Laufzeit-/CLI-Verhaltensänderung; Stage 29 ist eine Architekturvertrags- und Prüfmetadaten-Schicht",
    )


def _names_from_attr(bundle, attr: str) -> tuple[str, ...]:
    if bundle is None:
        return ()
    return tuple(sorted(getattr(item, "name", "") for item in getattr(bundle, attr, ()) if getattr(item, "name", "")))


def _capsule_names(architecture_map) -> tuple[str, ...]:
    if architecture_map is None:
        return ()
    return tuple(sorted(getattr(item, "name", "") for item in getattr(architecture_map, "capsules", ()) if getattr(item, "name", "")))


def _validation(diagrams: Sequence[CommutativeDiagramSpec], contracts: Sequence[CapsuleContractSpec], category_theory=None, architecture_map=None) -> ContractValidationSpec:
    known_capsules = _capsule_names(architecture_map)
    known_categories = _names_from_attr(category_theory, "categories")
    known_functors = _names_from_attr(category_theory, "functors")
    known_natural_transformations = _names_from_attr(category_theory, "natural_transformations")

    referenced_capsules = set()
    referenced_categories = set()
    referenced_functors = set()
    referenced_transformations = set()
    for diagram in diagrams:
        referenced_capsules.update(diagram.capsules)
        referenced_categories.update(diagram.categories)
        referenced_functors.update(diagram.functors)
        referenced_transformations.update(diagram.natural_transformations)
    for contract in contracts:
        referenced_capsules.add(contract.capsule)
        referenced_categories.add(contract.primary_category)
        primary = contract.primary_functor_or_transformation
        if primary.endswith("Transformation"):
            referenced_transformations.add(primary)
        else:
            referenced_functors.add(primary)

    if not (known_capsules or known_categories or known_functors or known_natural_transformations):
        return ContractValidationSpec("not_checked", known_capsules, known_categories, known_functors, known_natural_transformations, (), (), (), ())

    missing_capsules = tuple(sorted(referenced_capsules - set(known_capsules)))
    missing_categories = tuple(sorted(referenced_categories - set(known_categories)))
    missing_functors = tuple(sorted(referenced_functors - set(known_functors)))
    missing_transformations = tuple(sorted(referenced_transformations - set(known_natural_transformations)))
    status = "passed" if not (missing_capsules or missing_categories or missing_functors or missing_transformations) else "failed"
    return ContractValidationSpec(
        status=status,
        known_capsules=known_capsules,
        known_categories=known_categories,
        known_functors=known_functors,
        known_natural_transformations=known_natural_transformations,
        missing_capsules=missing_capsules,
        missing_categories=missing_categories,
        missing_functors=missing_functors,
        missing_natural_transformations=missing_transformations,
    )


def bootstrap_architecture_contracts(category_theory=None, architecture_map=None) -> ArchitectureContractsBundle:
    """Return the Stage-29 architecture contracts bundle."""

    if category_theory is None:
        from .category_theory import bootstrap_category_theory

        category_theory = bootstrap_category_theory()
    if architecture_map is None:
        from .architecture_map import bootstrap_architecture_map

        architecture_map = bootstrap_architecture_map()
    diagrams = _diagrams()
    contracts = _capsule_contracts()
    return ArchitectureContractsBundle(
        diagrams=diagrams,
        capsule_contracts=contracts,
        laws=_laws(),
        mermaid_diagram=_MERMAID_DIAGRAM,
        text_diagram=_TEXT_DIAGRAM,
        validation=_validation(diagrams, contracts, category_theory=category_theory, architecture_map=architecture_map),
        plan=_plan(),
    )
