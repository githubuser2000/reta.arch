from __future__ import annotations

"""Stage-28 architecture map for the Reta refactor.

Stage 27 named the categorical layer: categories, functors and natural
transformations.  Stage 28 draws the whole system around that layer.  Stage 29
adds explicit commutative diagrams and architecture laws over the map.  Stage 30
adds concrete witnesses that connect those laws back to repository files, probes
and tests.  The
objects here are intentionally lightweight metadata objects, just like the
Stage-27 category-theory module.  They answer three practical questions:

* Which legacy reta thing now belongs to which architecture capsule?
* What is contained inside what?
* Through which morphism / functor / natural-transformation path does data move?
"""

from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class ArchitectureCapsuleSpec:
    """One nested capsule in the refactored architecture."""

    name: str
    layer: str
    contains: Sequence[str]
    code_owners: Sequence[str]
    paradigm_roles: Sequence[str]
    inbound: Sequence[str]
    outbound: Sequence[str]
    stage_span: str
    description: str

    def snapshot(self) -> dict:
        return {
            "name": self.name,
            "layer": self.layer,
            "contains": list(self.contains),
            "code_owners": list(self.code_owners),
            "paradigm_roles": list(self.paradigm_roles),
            "inbound": list(self.inbound),
            "outbound": list(self.outbound),
            "stage_span": self.stage_span,
            "description": self.description,
        }


@dataclass(frozen=True)
class ArchitectureFlowSpec:
    """Directed architecture flow between two capsules."""

    source: str
    target: str
    morphism: str
    functor_or_transformation: str
    code_owner: str
    description: str

    def snapshot(self) -> dict:
        return {
            "source": self.source,
            "target": self.target,
            "morphism": self.morphism,
            "functor_or_transformation": self.functor_or_transformation,
            "code_owner": self.code_owner,
            "description": self.description,
        }


@dataclass(frozen=True)
class RetaPartMappingSpec:
    """Mapping from an old reta owner to its new architecture ownership."""

    legacy_owner: str
    old_responsibility: str
    new_capsule: str
    new_owner: Sequence[str]
    paradigm_role: Sequence[str]
    stage: str
    compatibility_surface: str
    notes: str

    def snapshot(self) -> dict:
        return {
            "legacy_owner": self.legacy_owner,
            "old_responsibility": self.old_responsibility,
            "new_capsule": self.new_capsule,
            "new_owner": list(self.new_owner),
            "paradigm_role": list(self.paradigm_role),
            "stage": self.stage,
            "compatibility_surface": self.compatibility_surface,
            "notes": self.notes,
        }


@dataclass(frozen=True)
class StageArchitectureStep:
    """One stage in the staged refactor history."""

    stage: str
    focus: str
    moved_from: Sequence[str]
    moved_to: Sequence[str]
    capsule: str
    paradigm_shift: str

    def snapshot(self) -> dict:
        return {
            "stage": self.stage,
            "focus": self.focus,
            "moved_from": list(self.moved_from),
            "moved_to": list(self.moved_to),
            "capsule": self.capsule,
            "paradigm_shift": self.paradigm_shift,
        }


@dataclass(frozen=True)
class CapsuleContainmentSpec:
    """Explicit containment relation between two architecture capsules."""

    parent: str
    child: str
    relation: str

    def snapshot(self) -> dict:
        return {"parent": self.parent, "child": self.child, "relation": self.relation}


@dataclass(frozen=True)
class MarkdownAuditSpec:
    """Record of the Markdown basis read for the stage."""

    source_package: str
    markdown_files_in_stage27_package: int
    uploaded_tar_markdown_files: int
    important_families: Sequence[str]
    conclusion: str

    def snapshot(self) -> dict:
        return {
            "source_package": self.source_package,
            "markdown_files_in_stage27_package": self.markdown_files_in_stage27_package,
            "uploaded_tar_markdown_files": self.uploaded_tar_markdown_files,
            "important_families": list(self.important_families),
            "conclusion": self.conclusion,
        }


@dataclass(frozen=True)
class ArchitectureMapBundle:
    """Inspectable total architecture map introduced in Stage 28."""

    capsules: Sequence[ArchitectureCapsuleSpec]
    containment: Sequence[CapsuleContainmentSpec]
    flows: Sequence[ArchitectureFlowSpec]
    legacy_mappings: Sequence[RetaPartMappingSpec]
    stage_steps: Sequence[StageArchitectureStep]
    mermaid_diagram: str
    text_diagram: str
    markdown_audit: MarkdownAuditSpec

    def capsule_named(self, name: str) -> ArchitectureCapsuleSpec:
        for capsule in self.capsules:
            if capsule.name == name:
                return capsule
        raise KeyError(f"Unknown architecture capsule: {name}")

    def snapshot(self) -> dict:
        return {
            "class": type(self).__name__,
            "stage": 30,
            "purpose": "Gesamtarchitektur, Kapselstruktur, reta-zu-Paradigma-Zuordnung, Datenflussdiagramm, Stage-29-Verträge und Stage-30-Witness-Matrix.",
            "counts": {
                "capsules": len(self.capsules),
                "containment": len(self.containment),
                "flows": len(self.flows),
                "legacy_mappings": len(self.legacy_mappings),
                "stage_steps": len(self.stage_steps),
            },
            "capsules": [item.snapshot() for item in self.capsules],
            "containment": [item.snapshot() for item in self.containment],
            "flows": [item.snapshot() for item in self.flows],
            "legacy_mappings": [item.snapshot() for item in self.legacy_mappings],
            "stage_steps": [item.snapshot() for item in self.stage_steps],
            "diagrams": {
                "text": self.text_diagram,
                "mermaid": self.mermaid_diagram,
            },
            "markdown_audit": self.markdown_audit.snapshot(),
        }


def _capsule(
    name: str,
    layer: str,
    contains: Sequence[str],
    code_owners: Sequence[str],
    paradigm_roles: Sequence[str],
    inbound: Sequence[str],
    outbound: Sequence[str],
    stage_span: str,
    description: str,
) -> ArchitectureCapsuleSpec:
    return ArchitectureCapsuleSpec(
        name=name,
        layer=layer,
        contains=tuple(contains),
        code_owners=tuple(code_owners),
        paradigm_roles=tuple(paradigm_roles),
        inbound=tuple(inbound),
        outbound=tuple(outbound),
        stage_span=stage_span,
        description=description,
    )


def _capsules() -> tuple[ArchitectureCapsuleSpec, ...]:
    return (
        _capsule(
            "RetaArchitectureRoot",
            "0 root / facade",
            (
                "SchemaTopologyCapsule",
                "LocalSectionCapsule",
                "SemanticSheafCapsule",
                "InputPromptCapsule",
                "WorkflowGluingCapsule",
                "TableCoreCapsule",
                "GeneratedRelationCapsule",
                "OutputRenderingCapsule",
                "CompatibilityCapsule",
                "CategoricalMetaCapsule",
            ),
            ("reta_architecture/facade.py", "reta_architecture/__init__.py"),
            ("Gesamtfunktor-Fassade", "Kapsel-Root"),
            ("Legacy CLI/Prompt/import paths",),
            ("architecture snapshot", "runtime bundles", "probe JSON"),
            "Stages 1-30",
            "Die oberste Fassade hält die neue Architektur zusammen und ersetzt den alten impliziten Monolithverbund als Orientierungspunkt.",
        ),
        _capsule(
            "SchemaTopologyCapsule",
            "1 schema + topology",
            ("RetaContextSchema", "ContextSelection", "RetaContextTopology", "split i18n modules", "tag/domain skeleton"),
            (
                "reta_architecture/schema.py",
                "reta_architecture/topology.py",
                "reta_architecture/split_i18n.py",
                "i18n/words_context.py",
                "i18n/words_matrix.py",
                "i18n/words_runtime.py",
            ),
            ("Topologie", "math Kategorie: OpenRetaContextCategory"),
            ("legacy i18n words data", "CLI/prompt language domains"),
            ("open contexts", "basis covers", "schema snapshot"),
            "Stages 1-4",
            "Hier werden die früher verstreuten Parameter-, Sprach-, Zeilen-, Ausgabe- und Scope-Domänen zu offenen Kontexten über reta.",
        ),
        _capsule(
            "LocalSectionCapsule",
            "2 presheaves / local data",
            ("FilesystemPresheaf", "PromptStatePresheaf", "LocalSection", "CSV sections", "translation/readme/assets sections"),
            ("reta_architecture/presheaves.py", "csv/*.csv", "doc/*.md", "readme*.md"),
            ("Prägarbe", "Restriktionsmorphismus", "LocalSectionCategory"),
            ("open contexts", "filesystem", "prompt raw text"),
            ("restricted local sections", "presheaf snapshot"),
            "Stage 1 onward",
            "Rohdaten bleiben lokal: CSVs, Übersetzungen, Assets und Prompt-Zustand werden als kontextabhängige Sektionen verstanden.",
        ),
        _capsule(
            "SemanticSheafCapsule",
            "3 sheaves / canonical semantics",
            (
                "ParameterSemanticsSheaf",
                "GeneratedColumnsSheaf",
                "TableOutputSheaf",
                "HtmlReferenceSheaf",
                "ParameterSemanticsBuilder",
            ),
            ("reta_architecture/sheaves.py", "reta_architecture/semantics_builder.py"),
            ("Garbe", "Sheafification", "CanonicalSemanticSheafCategory"),
            ("local sections", "schema topology", "legacy parameter matrices"),
            ("canonical pairs", "column numbers", "global semantic dictionaries"),
            "Stages 1-3 and 27",
            "Lokale Matrix-/CSV-/Aliasdaten werden zu kanonischer, global nutzbarer Parametersemantik verklebt.",
        ),
        _capsule(
            "InputPromptCapsule",
            "4 input + prompt stack",
            (
                "InputBundle",
                "RowRangeSyntax",
                "PromptVocabulary",
                "PromptRuntimeBundle",
                "CompletionRuntimeBundle",
                "PromptLanguageBundle",
                "PromptSessionBundle",
                "PromptExecutionBundle",
                "PromptPreparationBundle",
                "PromptInteractionBundle",
            ),
            (
                "reta_architecture/input_semantics.py",
                "reta_architecture/prompt_runtime.py",
                "reta_architecture/completion_runtime.py",
                "reta_architecture/prompt_language.py",
                "reta_architecture/prompt_session.py",
                "reta_architecture/prompt_execution.py",
                "reta_architecture/prompt_preparation.py",
                "reta_architecture/prompt_interaction.py",
                "retaPrompt.py",
                "libs/LibRetaPrompt.py",
                "libs/nestedAlx.py",
            ),
            ("Morphismen", "RawCommandPresheafFunctor", "RawToCanonicalParameterTransformation"),
            ("raw CLI/prompt text", "interactive session state", "completion requests"),
            ("canonical command tokens", "prompt execution calls", "row/column requests"),
            "Stages 4, 6-12",
            "Der alte Prompt-Monolith ist in Runtime, Completion, Sprache, Session, Execution, Vorbereitung und Interaktion gekapselt.",
        ),
        _capsule(
            "WorkflowGluingCapsule",
            "5 universal workflow / gluing",
            (
                "ParameterRuntimeBundle",
                "ColumnSelectionBundle",
                "ProgramWorkflowBundle",
                "TableGenerationBundle",
                "UniversalBundle",
                "merge_parameter_dicts",
                "normalize_column_buckets",
            ),
            (
                "reta_architecture/parameter_runtime.py",
                "reta_architecture/column_selection.py",
                "reta_architecture/program_workflow.py",
                "reta_architecture/table_generation.py",
                "reta_architecture/universal.py",
                "reta.py",
            ),
            ("universelle Eigenschaft", "Gluing", "TableGenerationGluingFunctor", "TableGenerationGluingTransformation"),
            ("canonical semantics", "CLI arguments", "selected rows/columns"),
            ("global table section", "workflow result", "table generation snapshot"),
            "Stages 2, 13-15, 19, 21",
            "Diese Kapsel ersetzt die früher in reta.py versteckte Orchestrierung durch kanonische Merge-/Normalisierungs-/Tabellenbau-Knoten.",
        ),
        _capsule(
            "TableCoreCapsule",
            "6 global table section + state",
            (
                "Tables",
                "TableRuntimeBundle",
                "TableStateBundle",
                "TableStateSections",
                "GeneratedColumnSection",
                "TableDisplayState",
                "TablePreparationBundle",
                "RowFilteringBundle",
                "TableWrappingBundle",
                "NumberTheoryBundle",
            ),
            (
                "reta_architecture/table_runtime.py",
                "reta_architecture/table_state.py",
                "reta_architecture/table_preparation.py",
                "reta_architecture/row_filtering.py",
                "reta_architecture/table_wrapping.py",
                "reta_architecture/number_theory.py",
                "libs/tableHandling.py",
                "libs/lib4tables_prepare.py",
            ),
            ("globale Garbensektion", "Tabellen-Morphismen", "ExplicitTableStateFunctor", "TableRuntimeToStateSectionsTransformation"),
            ("workflow gluing result", "generated-column effects", "row filters"),
            ("prepared table", "explicit state snapshot", "output-ready table"),
            "Stages 16, 20, 22-23, 25-26",
            "Die Tabelle ist jetzt eine globale Sektion mit explizitem Zustand; alte mutable Attribute bleiben nur noch Kompatibilitätsoberfläche.",
        ),
        _capsule(
            "GeneratedRelationCapsule",
            "7 generated/meta/concat/combi morphisms",
            (
                "GeneratedColumnsBundle",
                "GeneratedColumnRegistry",
                "MetaColumnsBundle",
                "ConcatCsvBundle",
                "KombiJoinBundle",
                "fraction/csv gluing morphisms",
                "generated table endomorphisms",
            ),
            (
                "reta_architecture/generated_columns.py",
                "reta_architecture/meta_columns.py",
                "reta_architecture/concat_csv.py",
                "reta_architecture/combi_join.py",
                "libs/lib4tables_concat.py",
                "libs/tableHandling.py",
            ),
            ("Morphismen", "Endofunktoren", "GeneratedColumnEndomorphismCategory", "GeneratedColumnsSheafSyncTransformation"),
            ("global table section", "local CSV sections", "selected generated parameters"),
            ("enriched table section", "generated-column state", "combi-joined table"),
            "Stages 17-19, 21",
            "Alle ehemals im Concat-/Combi-Monolithen liegenden Erzeuger werden als Tabellen-Endomorphismen oder CSV-Gluing-Morphismen geführt.",
        ),
        _capsule(
            "OutputRenderingCapsule",
            "8 syntax + output rendering",
            (
                "OutputSyntaxBundle",
                "RetaOutputSemantics",
                "TableOutputBundle",
                "TableOutput",
                "shell/markdown/html/csv/emacs/bbcode/nichts modes",
            ),
            (
                "reta_architecture/output_syntax.py",
                "reta_architecture/output_semantics.py",
                "reta_architecture/table_output.py",
                "libs/lib4tables.py",
            ),
            ("Renderer-Morphismus", "OutputRenderingFunctorFamily", "RenderedOutputNormalizationTransformation"),
            ("prepared global table", "output mode selection"),
            ("rendered output", "normalized parity output"),
            "Stages 5, 20, 24, 27",
            "Ausgabeformate sind nicht mehr Tabellenbesitz, sondern Darstellungsmorphismen über der globalen Tabellensektion.",
        ),
        _capsule(
            "CompatibilityCapsule",
            "9 legacy compatibility + parity",
            ("reta.py", "retaPrompt.py", "libs facades", "tests/test_command_parity.py", "RepoManifest"),
            (
                "reta.py",
                "retaPrompt.py",
                "libs/tableHandling.py",
                "libs/lib4tables.py",
                "libs/lib4tables_prepare.py",
                "libs/lib4tables_concat.py",
                "reta_architecture/package_integrity.py",
                "tests/test_command_parity.py",
            ),
            ("LegacyRuntimeFunctor", "ArchitectureRuntimeFunctor", "LegacyToArchitectureTransformation"),
            ("old import paths", "old command lines", "original archive"),
            ("same observable output", "package audit", "compatibility snapshots"),
            "Stages 3-28",
            "Die alte Oberfläche bleibt bedienbar; die Eigentümerschaft liegt schrittweise in den neuen Kapseln.",
        ),
        _capsule(
            "CategoricalMetaCapsule",
            "10 category theory + map",
            (
                "CategoryTheoryBundle",
                "CategorySpec",
                "FunctorSpec",
                "NaturalTransformationSpec",
                "ArchitectureMapBundle",
                "ArchitectureContractsBundle",
                "ArchitectureWitnessBundle",
                "CommutativeDiagramSpec",
                "CapsuleContractSpec",
                "RefactorLawSpec",
                "AnchorWitnessSpec",
                "CapsuleSliceSpec",
                "DiagramWitnessSpec",
                "capsule diagram",
            ),
            ("reta_architecture/category_theory.py", "reta_architecture/architecture_map.py", "reta_architecture/architecture_contracts.py", "reta_architecture/architecture_witnesses.py"),
            ("math Kategorie", "Funktor", "natürliche Transformation", "kommutierendes Diagramm", "Architekturkarte", "Witness"),
            ("all architecture bundles", "stage markdown history"),
            ("category-theory-json", "architecture-map-json", "architecture-diagram-md", "architecture-contracts-json", "architecture-contracts-md", "architecture-witnesses-json", "architecture-witnesses-md"),
            "Stages 27-30",
            "Diese Ebene benennt mathematische Objekte, zeigt die Kapselung, hält seit Stage 29 kommutierende Pfade als Gesetze fest und verbindet sie seit Stage 30 mit konkreten Witnesses.",
        ),
    )


def _containment() -> tuple[CapsuleContainmentSpec, ...]:
    child_names = (
        "SchemaTopologyCapsule",
        "LocalSectionCapsule",
        "SemanticSheafCapsule",
        "InputPromptCapsule",
        "WorkflowGluingCapsule",
        "TableCoreCapsule",
        "GeneratedRelationCapsule",
        "OutputRenderingCapsule",
        "CompatibilityCapsule",
        "CategoricalMetaCapsule",
    )
    return tuple(
        CapsuleContainmentSpec(
            parent="RetaArchitectureRoot",
            child=child,
            relation="RetaArchitecture bootstraps, owns or exposes this capsule through a bundle/probe snapshot.",
        )
        for child in child_names
    ) + (
        CapsuleContainmentSpec("SchemaTopologyCapsule", "LocalSectionCapsule", "Local sections are indexed over open contexts."),
        CapsuleContainmentSpec("LocalSectionCapsule", "SemanticSheafCapsule", "Compatible local sections glue into sheaves."),
        CapsuleContainmentSpec("SemanticSheafCapsule", "WorkflowGluingCapsule", "Canonical semantics drives workflow and table generation."),
        CapsuleContainmentSpec("WorkflowGluingCapsule", "TableCoreCapsule", "Universal workflow constructs the global table section."),
        CapsuleContainmentSpec("TableCoreCapsule", "GeneratedRelationCapsule", "Generated/meta/concat/combi morphisms act on table sections."),
        CapsuleContainmentSpec("TableCoreCapsule", "OutputRenderingCapsule", "Prepared table sections are rendered by output morphisms."),
        CapsuleContainmentSpec("CompatibilityCapsule", "RetaArchitectureRoot", "Legacy surfaces route into the architecture root and parity tests check commutation."),
        CapsuleContainmentSpec("CategoricalMetaCapsule", "RetaArchitectureRoot", "The meta layer describes the whole root without owning runtime behaviour."),
        CapsuleContainmentSpec("CategoricalMetaCapsule", "ArchitectureContractsBundle", "Stage 29 stores commutative diagrams, capsule contracts and refactor laws inside the categorical meta layer."),
        CapsuleContainmentSpec("CategoricalMetaCapsule", "ArchitectureWitnessBundle", "Stage 30 stores concrete repository witnesses for diagrams, laws, natural transformations and capsule slices."),
    )


def _flow(source: str, target: str, morphism: str, functor: str, owner: str, description: str) -> ArchitectureFlowSpec:
    return ArchitectureFlowSpec(
        source=source,
        target=target,
        morphism=morphism,
        functor_or_transformation=functor,
        code_owner=owner,
        description=description,
    )


def _flows() -> tuple[ArchitectureFlowSpec, ...]:
    return (
        _flow(
            "CompatibilityCapsule",
            "SchemaTopologyCapsule",
            "bootstrap schema from split i18n modules",
            "SchemaToTopologyFunctor",
            "RetaArchitecture.bootstrap + RetaContextSchema.from_words_parts",
            "Legacy words/context/matrix/runtime data becomes the typed topology base.",
        ),
        _flow(
            "SchemaTopologyCapsule",
            "LocalSectionCapsule",
            "restrict/open_for/cover_for_main",
            "LocalDataPresheafFunctor",
            "RetaContextTopology + PresheafBundle",
            "Open contexts index local files, prompt state and translation sections.",
        ),
        _flow(
            "LocalSectionCapsule",
            "SemanticSheafCapsule",
            "sheafification/gluing of compatible sections",
            "PresheafToSheafGluingTransformation",
            "PresheafBundle + SheafBundle + UniversalBundle",
            "Local CSV/translation/prompt sections are glued to global semantic sheaves.",
        ),
        _flow(
            "InputPromptCapsule",
            "SemanticSheafCapsule",
            "alias and prompt-token canonicalization",
            "RawToCanonicalParameterTransformation",
            "morphisms.py + prompt_language.py + sheaves.py",
            "Raw prompt or CLI text becomes canonical parameter semantics.",
        ),
        _flow(
            "SemanticSheafCapsule",
            "WorkflowGluingCapsule",
            "column selection + parameter runtime + universal merge",
            "TableGenerationGluingTransformation",
            "column_selection.py + parameter_runtime.py + universal.py",
            "Canonical pairs and local parameter dictionaries become normalized workflow input.",
        ),
        _flow(
            "WorkflowGluingCapsule",
            "TableCoreCapsule",
            "create/prepare global table section",
            "TableGenerationGluingFunctor",
            "table_generation.py + program_workflow.py + table_runtime.py",
            "The universal workflow creates the mutable-but-owned global table section.",
        ),
        _flow(
            "TableCoreCapsule",
            "GeneratedRelationCapsule",
            "generated columns / CSV concat / combi join",
            "GeneratedColumnEndofunctorFamily",
            "generated_columns.py + concat_csv.py + combi_join.py",
            "Table sections are enriched by generated, meta, fractional and combination morphisms.",
        ),
        _flow(
            "GeneratedRelationCapsule",
            "TableCoreCapsule",
            "sync generated metadata into explicit table state",
            "GeneratedColumnsSheafSyncTransformation",
            "generated_columns.py + table_state.py + universal.py",
            "Generated-column effects are mirrored into explicit state sections and sheaf metadata.",
        ),
        _flow(
            "TableCoreCapsule",
            "OutputRenderingCapsule",
            "render table output",
            "OutputRenderingFunctorFamily",
            "table_output.py + output_semantics.py + output_syntax.py",
            "Prepared table sections are rendered as shell, markdown, HTML, CSV, Emacs, BBCode or nothing.",
        ),
        _flow(
            "OutputRenderingCapsule",
            "CompatibilityCapsule",
            "normalize rendered output for parity",
            "RenderedOutputNormalizationTransformation",
            "tests/test_command_parity.py",
            "Renderer-specific syntax is normalized where needed for old-vs-new compatibility checks.",
        ),
        _flow(
            "CompatibilityCapsule",
            "RetaArchitectureRoot",
            "legacy facade delegation",
            "LegacyToArchitectureTransformation",
            "reta.py + retaPrompt.py + libs compatibility facades",
            "Old import and command paths keep working while delegating to the new owners.",
        ),
        _flow(
            "TableCoreCapsule",
            "CategoricalMetaCapsule",
            "runtime/state projection",
            "TableRuntimeToStateSectionsTransformation",
            "table_runtime.py + table_state.py + category_theory.py",
            "The mutable table runtime and the explicit table-state view are documented as a commutative projection.",
        ),
        _flow(
            "CategoricalMetaCapsule",
            "CompatibilityCapsule",
            "commutative architecture law checks",
            "LegacyToArchitectureTransformation",
            "architecture_contracts.py + tests/test_architecture_refactor.py",
            "Stage-29 diagrams state which category/functor/natural-transformation paths must keep commuting during later extractions.",
        ),
        _flow(
            "CategoricalMetaCapsule",
            "CompatibilityCapsule",
            "witness matrix ties contracts to files, tests and probes",
            "ContractedNaturalityTransformation",
            "architecture_witnesses.py + tests/test_architecture_refactor.py",
            "Stage-30 witnesses show where the architecture contracts are concretely evidenced in the repository.",
        ),
    )


def _mapping(
    legacy_owner: str,
    old_responsibility: str,
    new_capsule: str,
    new_owner: Sequence[str],
    paradigm_role: Sequence[str],
    stage: str,
    compatibility_surface: str,
    notes: str,
) -> RetaPartMappingSpec:
    return RetaPartMappingSpec(
        legacy_owner=legacy_owner,
        old_responsibility=old_responsibility,
        new_capsule=new_capsule,
        new_owner=tuple(new_owner),
        paradigm_role=tuple(paradigm_role),
        stage=stage,
        compatibility_surface=compatibility_surface,
        notes=notes,
    )


def _legacy_mappings() -> tuple[RetaPartMappingSpec, ...]:
    return (
        _mapping(
            "i18n/words.py",
            "Monolith für Sprache, Hauptparameter, Matrixdaten, Runtime-Konstanten und Kommandowörter.",
            "SchemaTopologyCapsule + SemanticSheafCapsule",
            ("i18n/words_context.py", "i18n/words_matrix.py", "i18n/words_runtime.py", "reta_architecture/schema.py", "reta_architecture/semantics_builder.py"),
            ("Topologie", "Prägarben-Index", "Garbe nach Semantik-Gluing"),
            "Stages 2-3",
            "i18n/words.py remains a compatibility facade.",
            "words.py liefert nicht mehr selbst die Architektur; die gesplitteten Module sind Quelle für Schema, Topologie und Semantik.",
        ),
        _mapping(
            "csv/*.csv",
            "Tabellenrohdaten für Religion, Primzahlen, Kombi, gebrochene Universen/Galaxien und Sprachvarianten.",
            "LocalSectionCapsule",
            ("reta_architecture/presheaves.py", "reta_architecture/concat_csv.py", "reta_architecture/table_generation.py"),
            ("Prägarbe", "LocalSection", "CSV-Gluing-Morphismus"),
            "Stages 1, 13, 19",
            "CSV file names stay unchanged.",
            "CSV-Dateien werden als lokale Sektionen gelesen und erst über Gluing in globale Tabellen-/Semantiksektionen gebracht.",
        ),
        _mapping(
            "reta.py",
            "CLI-Programm, Parameterparser, Semantikaufbau, Spaltenauswahl, Tabellenbau und Ausgabe-Orchestrierung.",
            "WorkflowGluingCapsule + CompatibilityCapsule",
            ("reta_architecture/parameter_runtime.py", "reta_architecture/column_selection.py", "reta_architecture/program_workflow.py", "reta_architecture/table_generation.py", "reta_architecture/facade.py"),
            ("universelle Eigenschaft", "Gluing", "ArchitectureRuntimeFunctor"),
            "Stages 2, 5, 13-15, 25-26",
            "reta.Program still exists and delegates to RetaArchitecture.",
            "reta.py wird zur CLI-/Legacy-Fassade; die großen Besitzerblöcke liegen in Architektur-Bundles.",
        ),
        _mapping(
            "retaPrompt.py",
            "Interaktive Prompt-Shell, Speicherlogik, Regex-Vorbereitung, Completion, Sprache und tiefe Ausführung.",
            "InputPromptCapsule",
            (
                "reta_architecture/prompt_runtime.py",
                "reta_architecture/completion_runtime.py",
                "reta_architecture/prompt_language.py",
                "reta_architecture/prompt_session.py",
                "reta_architecture/prompt_execution.py",
                "reta_architecture/prompt_preparation.py",
                "reta_architecture/prompt_interaction.py",
            ),
            ("RawCommandPresheafFunctor", "Prompt-Morphismen", "RawToCanonicalParameterTransformation"),
            "Stages 6-12",
            "retaPrompt.py remains the interactive entry surface.",
            "Prompt-Rohtext und Interaktion werden lokal gehalten, morphismisch normalisiert und dann an kanonische Semantik/Workflow übergeben.",
        ),
        _mapping(
            "libs/center.py",
            "Zeilenbereichs-Grammatik, zentrale Eingabe-/Hilfsdefinitionen und breite Legacy-Imports.",
            "InputPromptCapsule",
            ("reta_architecture/input_semantics.py", "reta_architecture/row_filtering.py"),
            ("Morphismen", "Restriktion auf Zeilenkontexte"),
            "Stages 4, 21-22",
            "center.py still exports legacy names and fallbacks.",
            "Die Eingabesyntax ist explizit; center.py bleibt Kompatibilitäts- und Fallback-Ort.",
        ),
        _mapping(
            "libs/LibRetaPrompt.py",
            "Prompt-Vokabular, Completion-Listen, promptsprachliche Hilfen und importzeitlicher Programmbau.",
            "InputPromptCapsule",
            ("reta_architecture/input_semantics.py", "reta_architecture/prompt_runtime.py", "reta_architecture/completion_runtime.py", "reta_architecture/prompt_language.py"),
            ("Prägarbe für Prompt-Zustand", "Prompt-Funktor", "Morphismen"),
            "Stages 4, 6-8",
            "LibRetaPrompt.py is now a thin compatibility facade.",
            "Der frühere Importzeit-Bootstrap wurde durch Architektur-Bundles ersetzt.",
        ),
        _mapping(
            "libs/nestedAlx.py",
            "Prompt-Completion-UI und verschachtelte Prompt-Hilfen.",
            "InputPromptCapsule",
            ("reta_architecture/completion_runtime.py", "reta_architecture/prompt_language.py"),
            ("Completion-Funktor", "Prompt-Sprachmorphismus"),
            "Stages 7-8",
            "nestedAlx.py consumes explicit prompt bundles.",
            "Nested UI bleibt Legacy-Consumer, aber nicht mehr Besitzer der Completion-Semantik.",
        ),
        _mapping(
            "libs/lib4tables.py",
            "Output-Syntaxklassen, Formatdetails und einzelne mathematische Hilfen.",
            "OutputRenderingCapsule + TableCoreCapsule",
            ("reta_architecture/output_syntax.py", "reta_architecture/output_semantics.py", "reta_architecture/number_theory.py"),
            ("Renderer-Morphismus", "OutputFormatCategory", "Zahlen-Morphismus"),
            "Stages 5, 23-24",
            "lib4tables.py remains a facade for legacy syntax names.",
            "Syntax und Semantik der Ausgabe sind getrennt; Zahlenhilfen gehören zur Tabellen-Morphismik.",
        ),
        _mapping(
            "libs/tableHandling.py",
            "Tables-God-Object, verschachtelte Output-/Combi-/Maintable-Logik und mutable Tabellenzustände.",
            "TableCoreCapsule + GeneratedRelationCapsule + OutputRenderingCapsule",
            ("reta_architecture/table_runtime.py", "reta_architecture/table_state.py", "reta_architecture/table_output.py", "reta_architecture/combi_join.py", "reta_architecture/generated_columns.py"),
            ("globale Garbensektion", "Endofunktor", "TableRuntimeToStateSectionsTransformation"),
            "Stages 20-21, 25-26",
            "libs/tableHandling.py re-exports compatible classes.",
            "Tables bleibt sichtbar, aber nicht mehr als unstrukturierter Besitzer aller Zustände und Operationen.",
        ),
        _mapping(
            "libs/lib4tables_prepare.py",
            "Prepare-Klasse mit Zeilenfiltern, Bereichslogik, Tabellenumbruch und Prepare-Ausgabe.",
            "TableCoreCapsule",
            ("reta_architecture/table_preparation.py", "reta_architecture/row_filtering.py", "reta_architecture/table_wrapping.py"),
            ("Tabellen-Morphismus", "Zeilenfilter-Morphismus", "universelle Vorbereitung"),
            "Stages 16, 22-23",
            "Prepare remains as delegation facade.",
            "Prepare wird von einer Implementierungsklasse zu einem Legacy-Adapter auf getrennte Morphismen.",
        ),
        _mapping(
            "libs/lib4tables_concat.py",
            "Generated Columns, Meta-Spalten, Bruch-/CSV-Gluing und Concat-Hilfen.",
            "GeneratedRelationCapsule",
            ("reta_architecture/generated_columns.py", "reta_architecture/meta_columns.py", "reta_architecture/concat_csv.py", "reta_architecture/combi_join.py"),
            ("Endofunktor", "CSV-Prägarben-Gluing", "GeneratedColumnEndomorphismCategory"),
            "Stages 17-19, 21",
            "Concat remains as compatibility wrapper.",
            "Concat-Methoden sind jetzt benannte Tabellenendomorphismen oder Gluing-Morphismen.",
        ),
        _mapping(
            "libs/lib4tables_Enum.py",
            "Tabellen-Tags und enumartige Markierungen.",
            "SchemaTopologyCapsule + GeneratedRelationCapsule",
            ("reta_architecture/schema.py", "reta_architecture/generated_columns.py", "reta_architecture/table_state.py"),
            ("Topologie-Tags", "Generated-column metadata", "Garbe"),
            "Stages 1, 17, 26",
            "Enum names stay import-compatible.",
            "Tags sind Teil der Kontext-Topologie und zugleich Metadaten der generierten Spalten.",
        ),
        _mapping(
            "reta_architecture/architecture_contracts.py",
            "Stage-29 Architekturverträge, kommutierende Quadrate, Kapselgrenzen und Referenzchecks über Kategorie- und Kapselkarte.",
            "CategoricalMetaCapsule",
            ("reta_architecture/architecture_contracts.py", "reta_architecture/category_theory.py", "reta_architecture/architecture_map.py"),
            ("kommutierendes Diagramm", "natürliche Transformation", "Refactor-Gesetz"),
            "Stage 29",
            "architecture-contracts-json and architecture-contracts-md expose the layer.",
            "Diese Datei besitzt keine Runtime-Semantik; sie hält fest, welche Pfade beim weiteren Umbau kommutieren müssen.",
        ),
        _mapping(
            "reta_architecture/architecture_witnesses.py",
            "Stage-30 Witness-Matrix für Kapseln, Diagramme, natürliche Transformationen und Refactor-Gesetze.",
            "CategoricalMetaCapsule",
            ("reta_architecture/architecture_witnesses.py", "reta_architecture/architecture_contracts.py", "tests/test_architecture_refactor.py"),
            ("Witness", "Proof obligation", "natürliche Transformation"),
            "Stage 30",
            "architecture-witnesses-json and architecture-witnesses-md expose the layer.",
            "Diese Datei verbindet die mathematischen Verträge mit konkreten Repository-Ankern und Probe-Kommandos.",
        ),
        _mapping(
            "readme*.md / doc/*.md",
            "Benutzerdokumentation zu CLI, Prompt und Startdateien.",
            "LocalSectionCapsule + CategoricalMetaCapsule",
            ("doc/*.md", "ARCHITECTURE_REFACTOR*.md", "STAGE*_CHANGES.md"),
            ("lokale Dokument-Sektion", "Architekturhistorie"),
            "Stages 1-28",
            "Documentation files stay data/documentation assets.",
            "Stage 28 nutzt die Markdown-Historie als Basis für die Kapselkarte.",
        ),
    )


def _step(stage: str, focus: str, moved_from: Sequence[str], moved_to: Sequence[str], capsule: str, paradigm_shift: str) -> StageArchitectureStep:
    return StageArchitectureStep(stage, focus, tuple(moved_from), tuple(moved_to), capsule, paradigm_shift)


def _stage_steps() -> tuple[StageArchitectureStep, ...]:
    return (
        _step("Stage 1", "Topologie-/Garben-/Morphismen-Architektur initial angelegt", ("implicit monolith layout",), ("topology.py", "presheaves.py", "sheaves.py", "morphisms.py", "universal.py", "facade.py"), "SchemaTopologyCapsule + LocalSectionCapsule + SemanticSheafCapsule", "erste Benennung von Topologie, Prägarbe, Garbe, Morphismus und universeller Eigenschaft"),
        _step("Stage 2", "Schema und Parameter-Semantik-Builder", ("i18n/words.py", "reta.py storeParamtersForColumns"), ("schema.py", "semantics_builder.py"), "SchemaTopologyCapsule + SemanticSheafCapsule", "Schema wird Quelle der Topologie; Semantikaufbau wird Gluing statt Programminline-Code"),
        _step("Stage 3", "Physischer i18n-Split", ("i18n/words.py monolith"), ("words_context.py", "words_matrix.py", "words_runtime.py", "words.py facade"), "SchemaTopologyCapsule", "Kontext-, Matrix- und Runtime-Sektionen werden getrennt"),
        _step("Stage 4", "Input-Semantik", ("center.py", "LibRetaPrompt.py"), ("input_semantics.py", "split_i18n.py"), "InputPromptCapsule", "Eingabe-Grammatik wird eigene Morphismenschicht"),
        _step("Stage 5", "Output-Semantik", ("reta.py output ladder", "tableHandling output booleans", "lib4tables syntax metadata"), ("output_semantics.py",), "OutputRenderingCapsule", "Ausgabemodi werden Renderer-Morphismen statt verstreuter Branches"),
        _step("Stage 6", "Prompt Runtime", ("LibRetaPrompt import-time Program",), ("prompt_runtime.py",), "InputPromptCapsule", "Prompt-Semantik entsteht aus Architektur statt aus vollem CLI-Programm"),
        _step("Stage 7", "Completion Runtime", ("spread prompt completion globals",), ("completion_runtime.py",), "InputPromptCapsule", "Completion wird eigene Laufzeitsektion"),
        _step("Stage 8", "Prompt Language", ("LibRetaPrompt helper block",), ("prompt_language.py",), "InputPromptCapsule", "Prompt-Sprache wird expliziter Morphismenblock"),
        _step("Stage 9", "Prompt Session", ("retaPrompt.py session/storage/input shell",), ("prompt_session.py",), "InputPromptCapsule", "Interaktive Session wird eigene lokale Zustandssektion"),
        _step("Stage 10", "Prompt Execution", ("retaPrompt.py deep command semantics",), ("prompt_execution.py",), "InputPromptCapsule", "tiefe Prompt-Kommandos werden ausführende Morphismen"),
        _step("Stage 11", "Prompt Preparation und Paketintegrität", ("retaPrompt.py preparation helpers",), ("prompt_preparation.py", "package_integrity.py"), "InputPromptCapsule + CompatibilityCapsule", "Vorbereitung und Manifest werden inspizierbare Architekturteile"),
        _step("Stage 12", "Prompt Interaction Controller", ("retaPrompt.py interaction loop",), ("prompt_interaction.py",), "InputPromptCapsule", "Prompt-Interaktion wird Orchestrationskapsel"),
        _step("Stage 13", "Spaltenauswahl und Tabellen-Gluing", ("reta.py column buckets", "reta.py table generation block"), ("column_selection.py", "table_generation.py"), "WorkflowGluingCapsule", "Spalten-/Tabellenbau wird universelles Gluing"),
        _step("Stage 14", "Parameter Runtime", ("reta.py CLI parser and upper-limit logic",), ("parameter_runtime.py",), "WorkflowGluingCapsule", "CLI-Parameter werden kanonische Runtime-Sektion"),
        _step("Stage 15", "Program Workflow", ("reta.py orchestration",), ("program_workflow.py",), "WorkflowGluingCapsule", "Programmablauf wird Workflow-Diagramm"),
        _step("Stage 16", "Table Preparation", ("lib4tables_prepare.py prepare output table",), ("table_preparation.py",), "TableCoreCapsule", "Prepare wird Tabellen-Morphismus"),
        _step("Stage 17", "Generated-column Morphismen", ("lib4tables_concat.py simple generated methods",), ("generated_columns.py",), "GeneratedRelationCapsule", "generierte Spalten werden Tabellen-Endomorphismen"),
        _step("Stage 18", "Schwere generated/meta columns", ("lib4tables_concat.py heavy generated/meta blocks",), ("generated_columns.py", "meta_columns.py"), "GeneratedRelationCapsule", "Meta-/Generated-Familien werden getrennte Morphismenkategorien"),
        _step("Stage 19", "CSV-/Bruch-Gluing", ("lib4tables_concat.py readConcatCsv/fraction helpers",), ("concat_csv.py",), "GeneratedRelationCapsule + WorkflowGluingCapsule", "CSV-Prägarben werden über Bruch-/Concat-Morphismen angeklebt"),
        _step("Stage 20", "Table Output", ("tableHandling.Tables.Output",), ("table_output.py",), "OutputRenderingCapsule", "Rendering wird Output-Morphismus über Tabellen-Sektion"),
        _step("Stage 21", "Combi Join und Gestirn-Spalte", ("tableHandling.Tables.Combi", "Maintable.createSpalteGestirn"), ("combi_join.py", "generated_columns.py"), "GeneratedRelationCapsule", "Kombi-Relationen werden Join-Morphismen; Gestirn wird Generated-Column-Morphismus"),
        _step("Stage 22", "Zeilenfilter-/Bereichsmorphismen", ("lib4tables_prepare.py row/range logic",), ("row_filtering.py",), "TableCoreCapsule", "Zeilenkontexte werden explizit gefilterte Sektionen"),
        _step("Stage 23", "Wrapping und Number Theory", ("prepare/table formatting helpers", "number-theory helper logic"), ("table_wrapping.py", "number_theory.py"), "TableCoreCapsule", "Zellumbruch und Zahlenlogik werden eigene Morphismen"),
        _step("Stage 24", "Output Syntax", ("lib4tables.py syntax classes",), ("output_syntax.py",), "OutputRenderingCapsule", "Ausgabe-Syntax wird von Ausgabe-Semantik getrennt"),
        _step("Stage 25", "Table Runtime", ("libs/tableHandling.py Tables owner",), ("table_runtime.py",), "TableCoreCapsule", "Tables wird globale Tabellensektion in der Architektur"),
        _step("Stage 26", "Explizite Table State Sections", ("mutable fields inside Tables",), ("table_state.py",), "TableCoreCapsule", "mutable Tabellenzustände werden explizite Sektionen"),
        _step("Stage 27", "Kategorien, Funktoren, natürliche Transformationen", ("implicit categorical structure",), ("category_theory.py",), "CategoricalMetaCapsule", "kommutierende Architekturpfade werden benannt"),
        _step("Stage 28", "Gesamtarchitektur als Kapselkarte", ("scattered stage documentation", "pure name list of math objects"), ("architecture_map.py", "architecture-map-json", "architecture-diagram-md"), "CategoricalMetaCapsule", "Topologie/Morphismen/Gluing/Garben/Kategorien/Funktoren/Transformationen werden als Schichten- und Datenflussdiagramm sichtbar"),
        _step("Stage 29", "Kommutierende Diagramme und Architekturgesetze", ("implicit naturality/parity contracts",), ("architecture_contracts.py", "architecture-contracts-json", "architecture-contracts-md"), "CategoricalMetaCapsule", "natürliche Transformationen werden als prüfbare kommutierende Refactor-Pfade und Gesetze sichtbar"),
        _step("Stage 30", "Witness-Matrix und konkrete Nachweise", ("symbolic contracts without repository witness matrix",), ("architecture_witnesses.py", "architecture-witnesses-json", "architecture-witnesses-md"), "CategoricalMetaCapsule", "Kategorien/Funktoren/natürliche Transformationen werden an konkrete reta-Dateien, Kapseln, Probes und Tests rückgebunden"),
    )


_TEXT_DIAGRAM = """\
RetaArchitectureRoot
├─ SchemaTopologyCapsule
│  ├─ i18n words_context / words_matrix / words_runtime
│  ├─ RetaContextSchema
│  └─ RetaContextTopology + ContextSelection
├─ LocalSectionCapsule
│  ├─ CSV / docs / translations / prompt raw state
│  └─ PresheafBundle(LocalSection, FilesystemPresheaf, PromptStatePresheaf)
├─ SemanticSheafCapsule
│  ├─ ParameterSemanticsSheaf
│  ├─ GeneratedColumnsSheaf
│  ├─ TableOutputSheaf
│  └─ HtmlReferenceSheaf
├─ InputPromptCapsule
│  ├─ InputBundle + RowRangeSyntax + PromptVocabulary
│  ├─ PromptRuntime + CompletionRuntime + PromptLanguage
│  └─ PromptSession + PromptExecution + PromptPreparation + PromptInteraction
├─ WorkflowGluingCapsule
│  ├─ ParameterRuntime
│  ├─ ColumnSelection
│  ├─ ProgramWorkflow
│  └─ TableGeneration + UniversalBundle
├─ TableCoreCapsule
│  ├─ TableRuntime.Tables = global table section
│  ├─ TableStateSections = explicit mutable sections
│  ├─ TablePreparation + RowFiltering + Wrapping
│  └─ NumberTheory
├─ GeneratedRelationCapsule
│  ├─ GeneratedColumns + MetaColumns
│  ├─ ConcatCsv / fractional CSV gluing
│  └─ KombiJoin
├─ OutputRenderingCapsule
│  ├─ OutputSyntax
│  ├─ OutputSemantics
│  └─ TableOutput renderers
├─ CompatibilityCapsule
│  ├─ reta.py / retaPrompt.py
│  ├─ libs compatibility facades
│  └─ parity + package integrity
└─ CategoricalMetaCapsule
   ├─ CategoryTheoryBundle
   ├─ ArchitectureMapBundle
   ├─ ArchitectureContractsBundle
   └─ ArchitectureWitnessBundle
"""


_MERMAID_DIAGRAM = """\
```mermaid
flowchart TD
    Legacy[Legacy surfaces<br/>reta.py / retaPrompt.py / libs] --> Root[RetaArchitectureRoot]
    Root --> Schema[SchemaTopologyCapsule<br/>schema + open contexts]
    Schema --> Presheaf[LocalSectionCapsule<br/>CSV/doc/prompt presheaves]
    Presheaf -->|PresheafToSheafGluingTransformation| Sheaf[SemanticSheafCapsule<br/>canonical semantic sheaves]
    Input[InputPromptCapsule<br/>CLI/prompt raw text] -->|RawToCanonicalParameterTransformation| Sheaf
    Sheaf -->|TableGenerationGluingTransformation| Workflow[WorkflowGluingCapsule<br/>parameter runtime + columns + table generation]
    Workflow --> Table[TableCoreCapsule<br/>Tables + explicit state sections]
    Table -->|GeneratedColumnEndofunctorFamily| Generated[GeneratedRelationCapsule<br/>generated/meta/concat/combi]
    Generated -->|GeneratedColumnsSheafSyncTransformation| Table
    Table -->|OutputRenderingFunctorFamily| Output[OutputRenderingCapsule<br/>shell/md/html/csv/...]
    Output -->|RenderedOutputNormalizationTransformation| Parity[CompatibilityCapsule<br/>legacy parity]
    Legacy -->|LegacyToArchitectureTransformation| Parity
    Meta[CategoricalMetaCapsule<br/>categories/functors/natural transformations/map/laws/witnesses] -. describes .-> Root
    Meta -. describes .-> Schema
    Meta -. describes .-> Sheaf
    Meta -. describes .-> Table
    Meta -. law checks .-> Parity
    Meta -. witness matrix .-> Parity
```
"""


def _markdown_audit() -> MarkdownAuditSpec:
    return MarkdownAuditSpec(
        source_package="Stage-27 repository package plus the newly uploaded tarball check",
        markdown_files_in_stage27_package=58,
        uploaded_tar_markdown_files=0,
        important_families=(
            "ARCHITECTURE_REFACTOR*.md",
            "STAGE*_CHANGES.md",
            "PACKAGE_AUDIT_STAGE*.md",
            "readme-reta*.md",
            "readme-retaPrompt*.md",
            "readme-startFiles.md",
        ),
        conclusion="The uploaded retaPyNewArch.tar.bz2 contains no Markdown files in this environment; Stage 28 is therefore based on the Stage-27 package Markdown history and records the tarball discrepancy explicitly.",
    )


def bootstrap_architecture_map() -> ArchitectureMapBundle:
    """Return the current staged total architecture and capsule map."""

    return ArchitectureMapBundle(
        capsules=_capsules(),
        containment=_containment(),
        flows=_flows(),
        legacy_mappings=_legacy_mappings(),
        stage_steps=_stage_steps(),
        mermaid_diagram=_MERMAID_DIAGRAM,
        text_diagram=_TEXT_DIAGRAM,
        markdown_audit=_markdown_audit(),
    )
