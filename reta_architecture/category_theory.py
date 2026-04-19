from __future__ import annotations

"""Symbolic category/functor/natural-transformation layer for the Reta architecture.

Stage 27 does not change runtime behaviour.  It makes the mathematical
architecture that the earlier stages already introduced explicit and
inspectable:

* topology: open Reta contexts and refinements
* presheaves/sheaves: local sections and glued global semantics
* morphisms/universal properties: transitions and gluing nodes
* categories/functors/natural transformations: structure-preserving maps between
  the above layers and commutative compatibility requirements

The classes in this module are deliberately lightweight metadata objects.  They
name the categorical structure of the current Python architecture without
turning every runtime function into a heavy framework object.
"""

from dataclasses import dataclass
from typing import Mapping, Sequence


@dataclass(frozen=True)
class CategoryObjectSpec:
    """Named object inside a symbolic architecture category."""

    name: str
    code_owner: str
    role: str

    def snapshot(self) -> dict:
        return {
            "name": self.name,
            "code_owner": self.code_owner,
            "role": self.role,
        }


@dataclass(frozen=True)
class CategoryMorphismSpec:
    """Named morphism inside a symbolic architecture category."""

    name: str
    source: str
    target: str
    code_owner: str
    role: str

    def snapshot(self) -> dict:
        return {
            "name": self.name,
            "source": self.source,
            "target": self.target,
            "code_owner": self.code_owner,
            "role": self.role,
        }


@dataclass(frozen=True)
class CategorySpec:
    """Symbolic category used by the Reta architecture."""

    name: str
    description: str
    objects: Sequence[CategoryObjectSpec]
    morphisms: Sequence[CategoryMorphismSpec]
    implemented_by: Sequence[str]

    def snapshot(self) -> dict:
        return {
            "name": self.name,
            "description": self.description,
            "objects": [item.snapshot() for item in self.objects],
            "morphisms": [item.snapshot() for item in self.morphisms],
            "implemented_by": list(self.implemented_by),
        }


@dataclass(frozen=True)
class FunctorSpec:
    """Symbolic functor between architecture categories."""

    name: str
    source_category: str
    target_category: str
    variance: str
    object_map: Mapping[str, str]
    morphism_map: Mapping[str, str]
    code_owner: str
    description: str

    def snapshot(self) -> dict:
        return {
            "name": self.name,
            "source_category": self.source_category,
            "target_category": self.target_category,
            "variance": self.variance,
            "object_map": dict(self.object_map),
            "morphism_map": dict(self.morphism_map),
            "code_owner": self.code_owner,
            "description": self.description,
        }


@dataclass(frozen=True)
class NaturalTransformationSpec:
    """Symbolic natural transformation between two architecture functors."""

    name: str
    source_functor: str
    target_functor: str
    components: Mapping[str, str]
    naturality_condition: str
    code_owner: str
    description: str

    def snapshot(self) -> dict:
        return {
            "name": self.name,
            "source_functor": self.source_functor,
            "target_functor": self.target_functor,
            "components": dict(self.components),
            "naturality_condition": self.naturality_condition,
            "code_owner": self.code_owner,
            "description": self.description,
        }


@dataclass(frozen=True)
class ParadigmTermSpec:
    """Project-local interpretation of one mathematical architecture term."""

    term: str
    meaning: str
    implemented_by: Sequence[str]
    stage_status: str

    def snapshot(self) -> dict:
        return {
            "term": self.term,
            "meaning": self.meaning,
            "implemented_by": list(self.implemented_by),
            "stage_status": self.stage_status,
        }


@dataclass(frozen=True)
class Stage27ArchitecturePlan:
    """Readable bridge between the previous plan and the Stage-27 implementation."""

    planned_before_stage_27: Sequence[str]
    implemented_in_stage_27: Sequence[str]
    already_implemented_before_stage_27: Sequence[str]
    behaviour_change: str

    def snapshot(self) -> dict:
        return {
            "planned_before_stage_27": list(self.planned_before_stage_27),
            "implemented_in_stage_27": list(self.implemented_in_stage_27),
            "already_implemented_before_stage_27": list(self.already_implemented_before_stage_27),
            "behaviour_change": self.behaviour_change,
        }


@dataclass(frozen=True)
class CategoryTheoryBundle:
    """Inspectable Stage-27 category-theory layer."""

    categories: Sequence[CategorySpec]
    functors: Sequence[FunctorSpec]
    natural_transformations: Sequence[NaturalTransformationSpec]
    paradigm_terms: Sequence[ParadigmTermSpec]
    plan: Stage27ArchitecturePlan

    def category_named(self, name: str) -> CategorySpec:
        return _find_by_name(self.categories, name, "category")

    def functor_named(self, name: str) -> FunctorSpec:
        return _find_by_name(self.functors, name, "functor")

    def natural_transformation_named(self, name: str) -> NaturalTransformationSpec:
        return _find_by_name(self.natural_transformations, name, "natural transformation")

    def snapshot(self) -> dict:
        return {
            "class": type(self).__name__,
            "paradigm": [
                "topology",
                "morphism",
                "universal_property",
                "presheaf",
                "sheaf",
                "category",
                "functor",
                "natural_transformation",
            ],
            "counts": {
                "categories": len(self.categories),
                "functors": len(self.functors),
                "natural_transformations": len(self.natural_transformations),
                "paradigm_terms": len(self.paradigm_terms),
            },
            "categories": [item.snapshot() for item in self.categories],
            "functors": [item.snapshot() for item in self.functors],
            "natural_transformations": [item.snapshot() for item in self.natural_transformations],
            "paradigm_terms": [item.snapshot() for item in self.paradigm_terms],
            "plan": self.plan.snapshot(),
        }


def _find_by_name(items, name: str, kind: str):
    for item in items:
        if item.name == name:
            return item
    raise KeyError(f"Unknown {kind}: {name}")


def _obj(name: str, code_owner: str, role: str) -> CategoryObjectSpec:
    return CategoryObjectSpec(name=name, code_owner=code_owner, role=role)


def _mor(name: str, source: str, target: str, code_owner: str, role: str) -> CategoryMorphismSpec:
    return CategoryMorphismSpec(name=name, source=source, target=target, code_owner=code_owner, role=role)


def _categories() -> tuple[CategorySpec, ...]:
    return (
        CategorySpec(
            name="OpenRetaContextCategory",
            description="Kategorie der offenen Reta-Kontexte; Morphismen sind Verfeinerungen, Einschränkungen und Basisüberdeckungen.",
            objects=(
                _obj("ContextSelection", "reta_architecture.topology.ContextSelection", "symbolische offene Kontextmenge"),
                _obj("RetaContextTopology", "reta_architecture.topology.RetaContextTopology", "Topologie über Sprache, Parametern, Zeilen, Ausgabearten und Scopes"),
                _obj("ContextCover", "reta_architecture.topology.RetaContextTopology.cover_for_main", "Basisüberdeckung eines Hauptparameter-Kontexts"),
            ),
            morphisms=(
                _mor("refine", "ContextSelection", "ContextSelection", "ContextSelection.refine", "Kontextverfeinerung"),
                _mor("open_for", "RetaContextTopology", "ContextSelection", "RetaContextTopology.open_for", "Basisöffnung erzeugen"),
                _mor("cover_for_main", "RetaContextTopology", "ContextCover", "RetaContextTopology.cover_for_main", "lokale Überdeckung erzeugen"),
            ),
            implemented_by=("reta_architecture/topology.py",),
        ),
        CategorySpec(
            name="LocalSectionCategory",
            description="Kategorie lokaler Rohsektionen; Morphismen sind Restriktionen entlang kleinerer Kontexte.",
            objects=(
                _obj("LocalSection", "reta_architecture.presheaves.LocalSection", "lokale CSV-/Übersetzungs-/Asset-/Prompt-Sektion"),
                _obj("FilesystemPresheaf", "reta_architecture.presheaves.FilesystemPresheaf", "Prägarbe lokaler Dateien"),
                _obj("PromptStatePresheaf", "reta_architecture.presheaves.PromptStatePresheaf", "Prägarbe lokaler Prompt-Zustände"),
            ),
            morphisms=(
                _mor("add_section", "LocalSection", "FilesystemPresheaf", "Presheaf.add_section", "lokale Sektion registrieren"),
                _mor("restrict", "FilesystemPresheaf", "LocalSection", "Presheaf.restrict", "Sektion auf Kontext einschränken"),
                _mor("update_prompt_state", "PromptStatePresheaf", "LocalSection", "PromptStatePresheaf.update", "Prompt-Rohsektion aktualisieren"),
            ),
            implemented_by=("reta_architecture/presheaves.py",),
        ),
        CategorySpec(
            name="CanonicalSemanticSheafCategory",
            description="Kategorie geklebter kanonischer Semantik; Morphismen lösen Aliasnamen, Parameterpaare und Spaltenmengen auf.",
            objects=(
                _obj("ParameterSemanticsSheaf", "reta_architecture.sheaves.ParameterSemanticsSheaf", "kanonische Parametersemantik"),
                _obj("GeneratedColumnsSheaf", "reta_architecture.sheaves.GeneratedColumnsSheaf", "Garbe generierter Spaltenmetadaten"),
                _obj("TableOutputSheaf", "reta_architecture.sheaves.TableOutputSheaf", "Garbe synchronisierter Ausgabe-Sektionen"),
                _obj("HtmlReferenceSheaf", "reta_architecture.sheaves.HtmlReferenceSheaf", "Garbe der HTML-Referenzen"),
            ),
            morphisms=(
                _mor("canonicalize_pair", "ParameterSemanticsSheaf", "CanonicalParameterPair", "ParameterSemanticsSheaf.canonicalize_pair", "Aliasauflösung zu kanonischem Paar"),
                _mor("column_numbers_for_pair", "CanonicalParameterPair", "ColumnNumberSet", "ParameterSemanticsSheaf.column_numbers_for_pair", "kanonisches Paar zu Spaltenmenge"),
                _mor("sync_from_tables", "Tables", "GeneratedColumnsSheaf", "GeneratedColumnsSheaf.sync_from_tables", "globale Tabellen-Metadaten in Garbe spiegeln"),
            ),
            implemented_by=("reta_architecture/sheaves.py", "reta_architecture/semantics_builder.py"),
        ),
        CategorySpec(
            name="UniversalConstructionCategory",
            description="Kategorie der Gluing-/Normalisierungs-Knoten, die lokale Sektionen zu globaler Semantik zusammenführen.",
            objects=(
                _obj("ParameterDictionaryDiagram", "reta_architecture.universal.merge_parameter_dicts", "Diagramm lokaler Parameter-Dictionaries"),
                _obj("ColumnBucketDiagram", "reta_architecture.universal.normalize_column_buckets", "Diagramm positiver/negativer Spaltenauswahl"),
                _obj("TableSyncDiagram", "reta_architecture.universal.UniversalBundle.sync_tables", "Diagramm globaler Tabellen-Synchronisierung"),
            ),
            morphisms=(
                _mor("merge_parameter_dicts", "ParameterDictionaryDiagram", "ParameterSemanticsSheaf", "reta_architecture.universal.merge_parameter_dicts", "pushout-artiges Zusammenkleben lokaler Parameterdaten"),
                _mor("normalize_column_buckets", "ColumnBucketDiagram", "NormalizedColumnBuckets", "reta_architecture.universal.normalize_column_buckets", "kanonische Differenz-/Normalisierungskonstruktion"),
                _mor("sync_tables", "Tables", "SheafBundle", "UniversalBundle.sync_tables", "globale Tabellen-Sektion in Garben synchronisieren"),
            ),
            implemented_by=("reta_architecture/universal.py", "reta_architecture/table_generation.py", "reta_architecture/program_workflow.py"),
        ),
        CategorySpec(
            name="TableSectionCategory",
            description="Kategorie globaler Tabellen- und Tabellenzustandssektionen; Morphismen sind Prepare-, Concat-, Join-, Zeilenfilter- und Output-Übergänge.",
            objects=(
                _obj("Tables", "reta_architecture.table_runtime.Tables", "mutable globale Tabellensektion"),
                _obj("TableStateSections", "reta_architecture.table_state.TableStateSections", "explizite Zustandssektionen der globalen Tabelle"),
                _obj("TablePreparationBundle", "reta_architecture.table_preparation.TablePreparationBundle", "Prepare-Morphismen"),
                _obj("TableOutput", "reta_architecture.table_output.TableOutput", "Renderer-naher Output-Morphismus"),
            ),
            morphisms=(
                _mor("prepare_output_table", "Tables", "Tables", "reta_architecture.table_preparation.prepare_output_table", "Tabellen-Prepare-Morphismus"),
                _mor("filter_original_lines", "ParameterSection", "RowSet", "reta_architecture.row_filtering.filter_original_lines", "Zeilenfilter-Morphismus"),
                _mor("readConcatCsv", "LocalCsvSection", "Tables", "reta_architecture.concat_csv.readConcatCsv", "CSV-Prägarbensektion in globale Tabelle kleben"),
                _mor("render_table_output", "Tables", "RenderedOutput", "reta_architecture.table_output.TableOutput", "Tabellensektion rendern"),
            ),
            implemented_by=(
                "reta_architecture/table_runtime.py",
                "reta_architecture/table_state.py",
                "reta_architecture/table_preparation.py",
                "reta_architecture/row_filtering.py",
                "reta_architecture/concat_csv.py",
                "reta_architecture/table_output.py",
            ),
        ),
        CategorySpec(
            name="GeneratedColumnEndomorphismCategory",
            description="Kategorie der generierten Spalten; Morphismen sind Endomorphismen der globalen Tabellensektion.",
            objects=(
                _obj("GeneratedColumnSpec", "reta_architecture.generated_columns.GeneratedColumnSpec", "Beschreibung eines generierten Spaltenmorphismus"),
                _obj("GeneratedColumnRegistry", "reta_architecture.generated_columns.GeneratedColumnRegistry", "Registry der Tabellen-Endomorphismen"),
                _obj("GeneratedColumnSection", "reta_architecture.table_state.GeneratedColumnSection", "Zustandssektion generierter Spalten"),
            ),
            morphisms=(
                _mor("concat_love_polygon", "Tables", "Tables", "reta_architecture.generated_columns.concat_love_polygon", "generiert Love-/Polygon-Spalten"),
                _mor("concat_modallogik", "Tables", "Tables", "reta_architecture.generated_columns.concat_modallogik", "generiert Modallogik-Spalten"),
                _mor("create_spalte_gestirn", "Tables", "Tables", "reta_architecture.generated_columns.create_spalte_gestirn", "generiert Gestirn-Spalte"),
            ),
            implemented_by=("reta_architecture/generated_columns.py", "reta_architecture/table_state.py"),
        ),
        CategorySpec(
            name="OutputFormatCategory",
            description="Kategorie konkreter Ausgabeformate und normalisierbarer Output-Sektionen.",
            objects=(
                _obj("OutputSyntax", "reta_architecture.output_syntax.OutputSyntax", "abstrakte Ausgabesyntax"),
                _obj("OutputModeSpec", "reta_architecture.output_semantics.OutputModeSpec", "semantische Ausgabeart"),
                _obj("RenderedOutput", "reta_architecture.table_output.TableOutput", "gerenderte Ausgabe"),
                _obj("NormalizedOutput", "tests.test_command_parity", "vergleichbare normalisierte Ausgabe"),
            ),
            morphisms=(
                _mor("apply_output_mode", "Tables", "OutputModeApplication", "reta_architecture.output_semantics.RetaOutputSemantics.apply_mode_to_tables", "Ausgabemodus auf Tabelle anwenden"),
                _mor("render", "Tables", "RenderedOutput", "reta_architecture.table_output.TableOutput", "globale Tabelle rendern"),
                _mor("normalize_for_parity", "RenderedOutput", "NormalizedOutput", "tests.test_command_parity", "Output für Paritätstests normalisieren"),
            ),
            implemented_by=("reta_architecture/output_syntax.py", "reta_architecture/output_semantics.py", "reta_architecture/table_output.py"),
        ),
        CategorySpec(
            name="LegacyFacadeCategory",
            description="Kategorie alter Import-/Aufrufpfade; Morphismen sind Kompatibilitätsdelegationen in die Architekturschicht.",
            objects=(
                _obj("reta.py Program", "reta.py", "historischer CLI-Einstieg"),
                _obj("libs.tableHandling", "libs/tableHandling.py", "alte Tabellen-Fassade"),
                _obj("libs.lib4tables_prepare", "libs/lib4tables_prepare.py", "alte Prepare-Fassade"),
                _obj("libs.lib4tables_concat", "libs/lib4tables_concat.py", "alte Concat-Fassade"),
            ),
            morphisms=(
                _mor("bootstrap_program", "reta.py Program", "RetaArchitecture", "reta.Program.__init__", "Programmlauf über Architektur-Fassade erzeugen"),
                _mor("tableHandling_reexport", "libs.tableHandling", "TableSectionCategory", "libs/tableHandling.py", "alte Tabellenimporte delegieren"),
                _mor("prepare_delegation", "libs.lib4tables_prepare", "TableSectionCategory", "libs/lib4tables_prepare.py", "alte Prepare-Methoden delegieren"),
                _mor("concat_delegation", "libs.lib4tables_concat", "GeneratedColumnEndomorphismCategory", "libs/lib4tables_concat.py", "alte Concat-Methoden delegieren"),
            ),
            implemented_by=("reta.py", "libs/tableHandling.py", "libs/lib4tables_prepare.py", "libs/lib4tables_concat.py"),
        ),

        CategorySpec(
            name="CommutativeArchitectureContractCategory",
            description="Kategorie der Stage-29-Architekturverträge; Objekte sind kommutierende Diagramme, Kapselgrenzen und Refactor-Gesetze.",
            objects=(
                _obj("CommutativeDiagramSpec", "reta_architecture.architecture_contracts.CommutativeDiagramSpec", "prüfbarer kommutierender Architekturpfad"),
                _obj("CapsuleContractSpec", "reta_architecture.architecture_contracts.CapsuleContractSpec", "Grenzvertrag einer Architektur-Kapsel"),
                _obj("RefactorLawSpec", "reta_architecture.architecture_contracts.RefactorLawSpec", "menschenlesbare Refactor-Invariante"),
                _obj("ArchitectureContractsBundle", "reta_architecture.architecture_contracts.ArchitectureContractsBundle", "gebündelte Stage-29-Vertragsmetadaten"),
            ),
            morphisms=(
                _mor("bootstrap_architecture_contracts", "CategoryTheoryBundle", "ArchitectureContractsBundle", "reta_architecture.architecture_contracts.bootstrap_architecture_contracts", "Vertragsbundle aus Kategorien und Kapselkarte erzeugen"),
                _mor("validate_contract_references", "ArchitectureContractsBundle", "ContractValidationSpec", "reta_architecture.architecture_contracts._validation", "Referenzen gegen bekannte Kategorien/Funktoren/Transformationen prüfen"),
                _mor("render_contract_diagram", "ArchitectureContractsBundle", "RenderedContractDiagram", "reta_architecture_probe_py.py architecture-contracts-md", "Vertragsdiagramm als Markdown/Mermaid ausgeben"),
            ),
            implemented_by=("reta_architecture/architecture_contracts.py",),
        ),
    )


def _functors() -> tuple[FunctorSpec, ...]:
    return (
        FunctorSpec(
            name="SchemaToTopologyFunctor",
            source_category="CanonicalSemanticSheafCategory",
            target_category="OpenRetaContextCategory",
            variance="covariant",
            object_map={
                "RetaContextSchema": "RetaContextTopology",
                "ParameterFamilies": "ContextSelection",
            },
            morphism_map={
                "schema_family_membership": "open_for",
                "main_parameter_cover": "cover_for_main",
            },
            code_owner="RetaContextTopology.from_schema",
            description="Erzeugt aus der kanonischen Schema-/Words-Struktur die Topologie der offenen Reta-Kontexte.",
        ),
        FunctorSpec(
            name="RawCommandPresheafFunctor",
            source_category="OpenRetaContextCategory",
            target_category="LocalSectionCategory",
            variance="contravariant",
            object_map={
                "ContextSelection": "LocalSection",
                "PromptText": "PromptStatePresheaf",
            },
            morphism_map={
                "refine": "restrict",
                "open_for": "add_section",
            },
            code_owner="reta_architecture.presheaves.PromptStatePresheaf",
            description="Ordnet jedem offenen Kontext lokale, noch nicht kanonisierte Prompt-/Datei-Sektionen zu.",
        ),
        FunctorSpec(
            name="CanonicalParameterSheafFunctor",
            source_category="OpenRetaContextCategory",
            target_category="CanonicalSemanticSheafCategory",
            variance="contravariant",
            object_map={
                "ContextSelection": "ParameterSemanticsSheaf",
                "ContextCover": "ParameterSemanticsSheaf",
            },
            morphism_map={
                "refine": "canonicalize_pair",
                "cover_for_main": "column_numbers_for_pair",
            },
            code_owner="reta_architecture.sheaves.ParameterSemanticsSheaf",
            description="Ordnet offenen Kontexten die geklebte kanonische Parametersemantik zu.",
        ),
        FunctorSpec(
            name="LocalDataPresheafFunctor",
            source_category="OpenRetaContextCategory",
            target_category="LocalSectionCategory",
            variance="contravariant",
            object_map={
                "ContextSelection": "FilesystemPresheaf",
                "CsvContext": "LocalSection",
            },
            morphism_map={
                "refine": "restrict",
                "cover_for_main": "add_section",
            },
            code_owner="reta_architecture.presheaves.FilesystemPresheaf",
            description="Modelliert CSVs, Übersetzungen und Assets als lokale Prägarben-Sektionen.",
        ),
        FunctorSpec(
            name="GluedSemanticSheafFunctor",
            source_category="OpenRetaContextCategory",
            target_category="CanonicalSemanticSheafCategory",
            variance="contravariant",
            object_map={
                "ContextSelection": "SheafBundle",
                "CsvContext": "ParameterSemanticsSheaf",
            },
            morphism_map={
                "refine": "sync_program_semantics",
                "cover_for_main": "merge_parameter_dicts",
            },
            code_owner="reta_architecture.sheaves.SheafBundle.from_repo",
            description="Klebt lokale Daten zu global verwendbarer Semantik.",
        ),
        FunctorSpec(
            name="TableGenerationGluingFunctor",
            source_category="UniversalConstructionCategory",
            target_category="TableSectionCategory",
            variance="covariant",
            object_map={
                "ParameterDictionaryDiagram": "Tables",
                "ColumnBucketDiagram": "TableStateSections",
            },
            morphism_map={
                "merge_parameter_dicts": "create_tables",
                "normalize_column_buckets": "prepare_output_table",
            },
            code_owner="reta_architecture.table_generation.bootstrap_table_generation",
            description="Führt Parameter- und Spaltenauswahl über universelles Gluing zur globalen Tabellen-Sektion.",
        ),
        FunctorSpec(
            name="GeneratedColumnEndofunctorFamily",
            source_category="TableSectionCategory",
            target_category="TableSectionCategory",
            variance="covariant",
            object_map={
                "Tables": "Tables",
                "GeneratedColumnSection": "GeneratedColumnSection",
            },
            morphism_map={
                "concat_love_polygon": "concat_love_polygon",
                "concat_modallogik": "concat_modallogik",
                "create_spalte_gestirn": "create_spalte_gestirn",
            },
            code_owner="reta_architecture.generated_columns.GeneratedColumnRegistry",
            description="Familie von Tabellen-Endofunktoren, die abgeleitete Spalten erzeugen.",
        ),
        FunctorSpec(
            name="OutputRenderingFunctorFamily",
            source_category="TableSectionCategory",
            target_category="OutputFormatCategory",
            variance="covariant",
            object_map={
                "Tables": "RenderedOutput",
                "TableStateSections": "OutputModeSpec",
            },
            morphism_map={
                "prepare_output_table": "render",
                "apply_output_mode": "apply_output_mode",
            },
            code_owner="reta_architecture.table_output.TableOutput",
            description="Renderer-Funktoren von globalen Tabellensektionen in konkrete Ausgabeformate.",
        ),
        FunctorSpec(
            name="NormalizedOutputFunctor",
            source_category="OutputFormatCategory",
            target_category="OutputFormatCategory",
            variance="covariant",
            object_map={
                "RenderedOutput": "NormalizedOutput",
                "OutputSyntax": "OutputSyntax",
            },
            morphism_map={
                "render": "normalize_for_parity",
                "apply_output_mode": "apply_output_mode",
            },
            code_owner="tests.test_command_parity",
            description="Vergleichsfunktor, der verschiedene Renderer-Ausgaben in paritätsfähige Normalformen überführt.",
        ),
        FunctorSpec(
            name="LegacyRuntimeFunctor",
            source_category="LegacyFacadeCategory",
            target_category="TableSectionCategory",
            variance="covariant",
            object_map={
                "libs.tableHandling": "Tables",
                "libs.lib4tables_prepare": "TablePreparationBundle",
                "libs.lib4tables_concat": "GeneratedColumnRegistry",
            },
            morphism_map={
                "tableHandling_reexport": "create_tables",
                "prepare_delegation": "prepare_output_table",
                "concat_delegation": "GeneratedColumnEndofunctorFamily",
            },
            code_owner="libs compatibility facades",
            description="Beschreibt, wie alte Importpfade auf die neue Tabellenarchitektur abgebildet werden.",
        ),
        FunctorSpec(
            name="ArchitectureRuntimeFunctor",
            source_category="LegacyFacadeCategory",
            target_category="TableSectionCategory",
            variance="covariant",
            object_map={
                "reta.py Program": "RetaArchitecture",
                "libs.tableHandling": "Tables",
                "libs.lib4tables_prepare": "TablePreparationBundle",
                "libs.lib4tables_concat": "GeneratedColumnRegistry",
            },
            morphism_map={
                "bootstrap_program": "bootstrap_table_runtime",
                "tableHandling_reexport": "create_tables",
                "prepare_delegation": "bootstrap_table_preparation",
                "concat_delegation": "bootstrap_generated_columns",
            },
            code_owner="reta_architecture.facade.RetaArchitecture",
            description="Der neue strukturierte Runtime-Pfad über die Architektur-Fassade.",
        ),
        FunctorSpec(
            name="MutableTableRuntimeFunctor",
            source_category="TableSectionCategory",
            target_category="TableSectionCategory",
            variance="covariant",
            object_map={
                "Tables": "Tables",
                "TableOutput": "TableOutput",
            },
            morphism_map={
                "prepare_output_table": "prepare_output_table",
                "render_table_output": "render_table_output",
            },
            code_owner="reta_architecture.table_runtime.Tables",
            description="Historisch-mutable Sicht der globalen Tabellensektion.",
        ),
        FunctorSpec(
            name="ExplicitTableStateFunctor",
            source_category="TableSectionCategory",
            target_category="TableSectionCategory",
            variance="covariant",
            object_map={
                "Tables": "TableStateSections",
                "GeneratedColumnSection": "GeneratedColumnSection",
            },
            morphism_map={
                "prepare_output_table": "TableStateSections.snapshot",
                "render_table_output": "TableStateSections.snapshot",
            },
            code_owner="reta_architecture.table_state.TableStateBundle",
            description="Projiziert die globale Runtime in explizite, inspizierbare Tabellenzustandssektionen.",
        ),

        FunctorSpec(
            name="CategoryTheoryToContractFunctor",
            source_category="CommutativeArchitectureContractCategory",
            target_category="CommutativeArchitectureContractCategory",
            variance="covariant",
            object_map={
                "CategoryTheoryBundle": "ArchitectureContractsBundle",
                "NaturalTransformationSpec": "CommutativeDiagramSpec",
            },
            morphism_map={
                "bootstrap_category_theory": "bootstrap_architecture_contracts",
                "natural_transformation_named": "diagram_named",
            },
            code_owner="reta_architecture.architecture_contracts.bootstrap_architecture_contracts",
            description="Hebt die Stage-27-Kategorien/Funktoren/natürlichen Transformationen in Stage-29-Vertragsdiagramme.",
        ),
        FunctorSpec(
            name="ArchitectureMapToContractFunctor",
            source_category="CommutativeArchitectureContractCategory",
            target_category="CommutativeArchitectureContractCategory",
            variance="covariant",
            object_map={
                "ArchitectureMapBundle": "ArchitectureContractsBundle",
                "ArchitectureCapsuleSpec": "CapsuleContractSpec",
                "ArchitectureFlowSpec": "CommutativeDiagramSpec",
            },
            morphism_map={
                "bootstrap_architecture_map": "bootstrap_architecture_contracts",
                "capsule_named": "capsule_contract_named",
            },
            code_owner="reta_architecture.architecture_contracts.bootstrap_architecture_contracts",
            description="Macht aus der Stage-28-Kapselkarte explizite Kapselverträge und kommutierende Diagramme.",
        ),
    )


def _natural_transformations() -> tuple[NaturalTransformationSpec, ...]:
    return (
        NaturalTransformationSpec(
            name="RawToCanonicalParameterTransformation",
            source_functor="RawCommandPresheafFunctor",
            target_functor="CanonicalParameterSheafFunctor",
            components={
                "PromptText": "PromptMorphisms.split_command_words",
                "RawAlias": "AliasMorphisms.canonical_main / canonical_sub",
                "ParameterPair": "ParameterSemanticsSheaf.canonicalize_pair",
            },
            naturality_condition="Kontext zuerst einschränken und dann kanonisieren liefert dieselbe kanonische Semantik wie zuerst kanonisieren und anschließend auf den kleineren Kontext einschränken.",
            code_owner="reta_architecture.morphisms + reta_architecture.sheaves",
            description="Macht CLI-/Prompt-Rohtext zu kanonischer Parametersemantik.",
        ),
        NaturalTransformationSpec(
            name="PresheafToSheafGluingTransformation",
            source_functor="LocalDataPresheafFunctor",
            target_functor="GluedSemanticSheafFunctor",
            components={
                "CsvSections": "Presheaf.restrict -> merge_parameter_dicts",
                "TranslationSections": "SheafBundle.from_repo",
                "PromptSections": "PromptStatePresheaf.update -> sync_program_semantics",
            },
            naturality_condition="Lokale Sektionen über einer Überdeckung kleben zu derselben globalen Semantik, unabhängig davon, in welcher kompatiblen Reihenfolge die lokalen Restriktionen gelesen werden.",
            code_owner="reta_architecture.presheaves + reta_architecture.sheaves + reta_architecture.universal",
            description="Symbolische Sheafification der bereits vorhandenen Prägarben in die geklebten Garben.",
        ),
        NaturalTransformationSpec(
            name="TableGenerationGluingTransformation",
            source_functor="CanonicalParameterSheafFunctor",
            target_functor="TableGenerationGluingFunctor",
            components={
                "ParameterSemanticsSheaf": "ColumnSelectionBundle",
                "ColumnBuckets": "normalize_column_buckets",
                "ProgramWorkflow": "ProgramWorkflowBundle.run",
            },
            naturality_condition="Kanonische Parametersemantik, Spaltenauswahl und Tabellenbau bilden ein kommutatives Workflow-Diagramm: äquivalente Alias-/Kontextpfade erzeugen dieselbe globale Tabellensektion.",
            code_owner="reta_architecture.column_selection + reta_architecture.table_generation + reta_architecture.program_workflow",
            description="Verbindet die geklebte Parametersemantik mit der globalen Tabellen-Sektion.",
        ),
        NaturalTransformationSpec(
            name="GeneratedColumnsSheafSyncTransformation",
            source_functor="GeneratedColumnEndofunctorFamily",
            target_functor="ExplicitTableStateFunctor",
            components={
                "GeneratedColumnRegistry": "GeneratedColumnSection.parameters",
                "GeneratedColumnTags": "GeneratedColumnSection.tags",
                "GeneratedColumnsSheaf": "sync_generated_columns_from_tables",
            },
            naturality_condition="Ein generierter Spalten-Endofunktor und die anschließende State-/Sheaf-Synchronisierung kommutieren mit dem direkten Zugriff auf die explizite GeneratedColumnSection.",
            code_owner="reta_architecture.generated_columns + reta_architecture.table_state + reta_architecture.universal",
            description="Hält generierte Spalten als Runtime-Zustand und als Garbenmetadaten zusammen.",
        ),
        NaturalTransformationSpec(
            name="TableRuntimeToStateSectionsTransformation",
            source_functor="MutableTableRuntimeFunctor",
            target_functor="ExplicitTableStateFunctor",
            components={
                "Tables.generatedSpaltenParameter": "TableStateSections.generated_columns.parameters",
                "Tables.generatedSpaltenParameter_Tags": "TableStateSections.generated_columns.tags",
                "Tables.rowNumDisplay2rowNumOrig": "TableStateSections.row_display_to_original",
                "Tables.religionNumbers": "TableDisplayState.religion_numbers",
            },
            naturality_condition="Alte mutable Tabellenattribute und neue explizite Zustandssektionen referenzieren dieselben Objekte; Mutation über einen Pfad ist über den anderen Pfad sichtbar.",
            code_owner="reta_architecture.table_runtime + reta_architecture.table_state",
            description="Formalisiert den Stage-26-Übergang von `Tables` zu expliziten Tabellenzustandssektionen.",
        ),
        NaturalTransformationSpec(
            name="RenderedOutputNormalizationTransformation",
            source_functor="OutputRenderingFunctorFamily",
            target_functor="NormalizedOutputFunctor",
            components={
                "html": "HTML normalisieren",
                "markdown": "Markdown-Text vergleichen",
                "shell": "Shell-Text vergleichen",
                "csv": "CSV-Text vergleichen",
            },
            naturality_condition="Renderer-Ausgaben dürfen syntaktische Formatdetails haben, müssen nach zulässiger Normalisierung aber dieselbe semantische Paritätsaussage ergeben.",
            code_owner="reta_architecture.output_syntax + reta_architecture.output_semantics + tests.test_command_parity",
            description="Macht die existierende Renderer-Parität als natürliche Transformation sichtbar.",
        ),
        NaturalTransformationSpec(
            name="LegacyToArchitectureTransformation",
            source_functor="LegacyRuntimeFunctor",
            target_functor="ArchitectureRuntimeFunctor",
            components={
                "reta.py": "RetaArchitecture.bootstrap",
                "libs.tableHandling": "reta_architecture.table_runtime",
                "libs.lib4tables_prepare": "reta_architecture.table_preparation / row_filtering / table_wrapping",
                "libs.lib4tables_concat": "reta_architecture.generated_columns / concat_csv / combi_join",
            },
            naturality_condition="Jeder repräsentative alte Aufrufpfad und der entsprechende neue Architekturpfad müssen beobachtbar gleiche Ausgabe liefern.",
            code_owner="compatibility facades + tests.test_command_parity",
            description="Die zentrale Refactor-Invariante: Legacy-Fassaden und Architektur-Fassade kommutieren beobachtbar.",
        ),

        NaturalTransformationSpec(
            name="ContractedNaturalityTransformation",
            source_functor="CategoryTheoryToContractFunctor",
            target_functor="ArchitectureMapToContractFunctor",
            components={
                "NaturalTransformationSpec": "CommutativeDiagramSpec",
                "ArchitectureCapsuleSpec": "CapsuleContractSpec",
                "RefactorInvariant": "RefactorLawSpec",
                "ReferenceValidation": "ContractValidationSpec",
            },
            naturality_condition="Die aus Kategorie-Theorie und Kapselkarte abgeleiteten Vertragsdiagramme referenzieren dieselben bekannten Kapseln, Kategorien, Funktoren und natürlichen Transformationen.",
            code_owner="reta_architecture.architecture_contracts",
            description="Stage 29 macht natürliche Transformationen zu expliziten, validierten Architekturverträgen.",
        ),
    )


def _paradigm_terms() -> tuple[ParadigmTermSpec, ...]:
    return (
        ParadigmTermSpec(
            term="Topologie",
            meaning="Reta-Kontexte als offene Mengen über Sprache, Parametern, Zeilen, Ausgabearten, Tags und Scopes.",
            implemented_by=("reta_architecture/topology.py",),
            stage_status="bereits seit früher Refactor-Stufe umgesetzt; Stage 27 macht die Kategorie der offenen Kontexte explizit",
        ),
        ParadigmTermSpec(
            term="Morphismus",
            meaning="Explizit benannte Übergänge zwischen Architektursektionen statt versteckter Methoden in Legacy-Klassen.",
            implemented_by=(
                "reta_architecture/morphisms.py",
                "reta_architecture/row_filtering.py",
                "reta_architecture/generated_columns.py",
                "reta_architecture/concat_csv.py",
                "reta_architecture/table_output.py",
            ),
            stage_status="bereits breit umgesetzt; Stage 27 ordnet Morphismen Kategorien und Funktoren zu",
        ),
        ParadigmTermSpec(
            term="universelle Eigenschaft",
            meaning="Kanonische Gluing-/Normalisierungs-Knoten, die lokale Daten kompatibel zusammenführen.",
            implemented_by=("reta_architecture/universal.py", "reta_architecture/table_generation.py", "reta_architecture/program_workflow.py"),
            stage_status="bereits umgesetzt; Stage 27 benennt die UniversalConstructionCategory",
        ),
        ParadigmTermSpec(
            term="Prägarbe",
            meaning="Lokale Rohsektionen, die über Kontext-Restriktionen gelesen werden.",
            implemented_by=("reta_architecture/presheaves.py",),
            stage_status="bereits umgesetzt; Stage 27 ergänzt Presheaf-Funktoren",
        ),
        ParadigmTermSpec(
            term="Garbe",
            meaning="Geklebte, global verwendbare Semantik aus lokalen Sektionen.",
            implemented_by=("reta_architecture/sheaves.py",),
            stage_status="bereits umgesetzt; Stage 27 ergänzt Sheafification als natürliche Transformation",
        ),
        ParadigmTermSpec(
            term="math Kategorie",
            meaning="Objekte und Morphismen der Architektur werden als inspizierbare Kategorien benannt.",
            implemented_by=("reta_architecture/category_theory.py",),
            stage_status="neu in Stage 27",
        ),
        ParadigmTermSpec(
            term="Funktor",
            meaning="Strukturerhaltende Abbildungen zwischen Kontext-, Sektionen-, Tabellen-, Output- und Legacy-Kategorien.",
            implemented_by=("reta_architecture/category_theory.py",),
            stage_status="neu in Stage 27",
        ),
        ParadigmTermSpec(
            term="natürliche Transformation",
            meaning="Kommutierende Verträglichkeitsfamilien zwischen Funktoren, z.B. Raw→Canonical, Presheaf→Sheaf, Legacy→Architecture.",
            implemented_by=("reta_architecture/category_theory.py",),
            stage_status="neu in Stage 27",
        ),
    )


def _plan() -> Stage27ArchitecturePlan:
    return Stage27ArchitecturePlan(
        planned_before_stage_27=(
            "Nicht noch eine große Verhaltensänderung, sondern die bereits extrahierten Topologie-/Prägarben-/Garben-/Morphismen-/Gluing-Schichten kategorial sichtbar machen.",
            "Kategorien für offene Kontexte, lokale Sektionen, geklebte Semantik, Tabellen-Sektionen, generierte Spalten, Ausgabeformate und Legacy-Fassaden benennen.",
            "Funktoren zwischen diesen Kategorien einführen, insbesondere Presheaf-/Sheaf-, Table-Generation-, Renderer- und Legacy-Kompatibilitätsfunktoren.",
            "Natürliche Transformationen ergänzen, weil die Refactor-Invariante nicht nur Funktorabbildung ist, sondern kommutierende Verträglichkeit zwischen alten/neuen und lokalen/globalen Pfaden.",
        ),
        implemented_in_stage_27=(
            "Neue Datei reta_architecture/category_theory.py mit CategorySpec, FunctorSpec, NaturalTransformationSpec, ParadigmTermSpec und CategoryTheoryBundle.",
            "RetaArchitecture bootstrapt und snapshottet jetzt die Kategorie-Theorie-Schicht.",
            "reta_architecture_probe_py.py besitzt category-theory-json.",
            "Paketmanifest und Regressionstests prüfen die neue Schicht.",
            "Dokumentation beschreibt geplant/jetzt/bereits umgesetzt.",
        ),
        already_implemented_before_stage_27=(
            "Topologie: reta_architecture/topology.py.",
            "Prägarben: reta_architecture/presheaves.py.",
            "Garben: reta_architecture/sheaves.py.",
            "Morphismen: morphisms.py, row_filtering.py, generated_columns.py, concat_csv.py, combi_join.py, table_output.py und weitere.",
            "Universelle Eigenschaften/Gluing: reta_architecture/universal.py, table_generation.py und program_workflow.py.",
            "Globale Tabellensektion und State-Sektionen: table_runtime.py und table_state.py.",
        ),
        behaviour_change="keine beabsichtigte Laufzeit-/CLI-Verhaltensänderung; Stage 27 ist eine explizite, inspizierbare Architektur- und Paradigmen-Schicht",
    )


def bootstrap_category_theory() -> CategoryTheoryBundle:
    """Return the Stage-27 categorical architecture metadata."""

    return CategoryTheoryBundle(
        categories=_categories(),
        functors=_functors(),
        natural_transformations=_natural_transformations(),
        paradigm_terms=_paradigm_terms(),
        plan=_plan(),
    )
