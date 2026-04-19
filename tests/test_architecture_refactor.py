from __future__ import annotations

import ast
import io
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(REPO_ROOT / "libs"))

import center  # noqa: E402
import LibRetaPrompt  # noqa: E402
import i18n.words as words  # noqa: E402
import i18n.words_context as words_context  # noqa: E402
import i18n.words_matrix as words_matrix  # noqa: E402
import i18n.words_runtime as words_runtime  # noqa: E402
import reta  # noqa: E402
import lib4tables  # noqa: E402
from reta_architecture import (  # noqa: E402
    ParameterSemanticsBuilder,
    PromptModus,
    RetaArchitecture,
    bootstrap_prompt_language,
    bootstrap_prompt_session,
    custom_split,
    custom_split2,
    is15or16command,
    isReTaParameter,
    stextFromKleinKleinKleinBefehl,
    verifyBruchNganzZahlBetweenCommas,
    verkuerze_dict,
)
from reta_architecture.prompt_execution import PromptExecutionBundle  # noqa: E402
from reta_architecture.prompt_preparation import PromptPreparationBundle  # noqa: E402
from reta_architecture.prompt_interaction import PromptInteractionBundle  # noqa: E402
from reta_architecture.parameter_runtime import ParameterRuntimeBundle  # noqa: E402
from reta_architecture.program_workflow import ProgramWorkflowBundle  # noqa: E402
from reta_architecture.table_preparation import TablePreparationBundle  # noqa: E402
from reta_architecture.table_wrapping import TableWrappingBundle  # noqa: E402
from reta_architecture.table_state import TableStateBundle  # noqa: E402
from reta_architecture.category_theory import CategoryTheoryBundle  # noqa: E402
from reta_architecture.architecture_map import ArchitectureMapBundle  # noqa: E402
from reta_architecture.architecture_contracts import ArchitectureContractsBundle  # noqa: E402
from reta_architecture.architecture_witnesses import ArchitectureWitnessBundle  # noqa: E402
from reta_architecture.table_output import TableOutputBundle  # noqa: E402
from reta_architecture.generated_columns import GeneratedColumnsBundle  # noqa: E402
from reta_architecture.meta_columns import MetaColumnsBundle  # noqa: E402
from reta_architecture.concat_csv import ConcatCsvBundle  # noqa: E402
from reta_architecture.combi_join import KombiJoinBundle  # noqa: E402
from reta_architecture.row_filtering import RowFilteringBundle  # noqa: E402
from reta_architecture.output_syntax import OutputSyntaxBundle  # noqa: E402
from reta_architecture.number_theory import NumberTheoryBundle, primCreativity as arch_prim_creativity, moonNumber as arch_moon_number  # noqa: E402
from reta_architecture.package_integrity import RepoManifest  # noqa: E402


class ArchitectureRefactorRegressionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.architecture = RetaArchitecture.bootstrap(REPO_ROOT)

    def _build_program(self):
        return reta.Program(["reta.py"], runAlles=False)

    def _semantic_program(self):
        return self.architecture.bootstrap_prompt_runtime(i18n=center.i18n).program

    def test_schema_is_explicit(self):
        schema = self.architecture.schema
        self.assertGreater(len(schema.language_aliases), 0)
        self.assertGreater(len(schema.parameters_main), 0)
        self.assertGreater(len(schema.para_n_data_matrix), 0)

    def test_words_split_modules_are_visible(self):
        schema = self.architecture.schema
        self.assertEqual(schema.schema_modules["context"], "i18n.words_context")
        self.assertEqual(schema.schema_modules["matrix"], "i18n.words_matrix")
        self.assertEqual(schema.schema_modules["runtime"], "i18n.words_runtime")
        self.assertEqual(words.MODULE_SPLIT["context"], "i18n.words_context")
        self.assertEqual(len(words.paraNdataMatrix), len(words_matrix.paraNdataMatrix))
        self.assertEqual(words.ParametersMain.alles, words_context.ParametersMain.alles)
        self.assertEqual(words.csvFileNames.religion, words_runtime.csvFileNames.religion)

    def test_input_layer_is_explicit(self):
        snapshot = self.architecture.snapshot()["inputs"]
        self.assertEqual(snapshot["row_ranges"]["multiple_prefix"], center.i18n.befehle2["v"])
        self.assertTrue(snapshot["prompt_vocabulary_builder"]["available"])

    def test_prompt_runtime_layer_is_explicit(self):
        prompt_runtime = self.architecture.bootstrap_prompt_runtime(i18n=center.i18n, force_rebuild=True)
        snapshot = prompt_runtime.snapshot()
        self.assertEqual(snapshot["program_view"]["class"], "PromptProgramView")
        self.assertEqual(snapshot["program_view"]["paraDict_len"], 4155)
        self.assertEqual(snapshot["program_view"]["dataDict_sizes"], [554, 46, 11, 12, 7, 23, 23, 10, 14, 23, 23, 12, 0, 0])
        self.assertTrue(snapshot["validation"]["wahl15_valid"])
        self.assertEqual(prompt_runtime.program.mainParaCmds, LibRetaPrompt.retaProgram.mainParaCmds)
        self.assertEqual(prompt_runtime.vocabulary.snapshot(), LibRetaPrompt.promptVocabulary.snapshot())
        program = self._semantic_program()
        self.assertEqual(prompt_runtime.program.dataDict[0], program.dataDict[0])
        self.assertEqual(prompt_runtime.program.kombiReverseDict, program.kombiReverseDict)
        self.assertEqual(prompt_runtime.program.kombiReverseDict2, program.kombiReverseDict2)
        self.assertEqual(prompt_runtime.program.AllSimpleCommandSpalten, program.AllSimpleCommandSpalten)


    def test_prompt_session_layer_is_explicit(self):
        prompt_session = self.architecture.bootstrap_prompt_session(i18n=center.i18n, force_rebuild=True)
        snapshot = prompt_session.snapshot()
        self.assertEqual(snapshot["class"], "PromptSessionBundle")
        self.assertEqual(snapshot["prompt_runtime_class"], "PromptRuntimeBundle")
        self.assertEqual(snapshot["completion_runtime_class"], "CompletionRuntimeBundle")
        self.assertEqual(snapshot["prompt_language_class"], "PromptLanguageBundle")
        text_state = prompt_session.new_text_state("p5")
        self.assertEqual(type(text_state).__name__, "PromptTextState")
        self.assertEqual(text_state.liste, ["p5"])

    def test_prompt_execution_layer_is_explicit(self):
        prompt_execution = self.architecture.bootstrap_prompt_execution(i18n=center.i18n, force_rebuild=True)
        snapshot = prompt_execution.snapshot()
        self.assertIsInstance(prompt_execution, PromptExecutionBundle)
        self.assertEqual(snapshot["class"], "PromptExecutionBundle")
        self.assertEqual(snapshot["command_runner"], "PromptGrosseAusgabe")
        self.assertEqual(snapshot["fraction_manager"], "bruchBereichsManagementAndWbefehl")
        self.assertEqual(snapshot["reta_executor"], "retaExecuteNprint")

    def test_prompt_preparation_layer_is_explicit(self):
        prompt_preparation = self.architecture.bootstrap_prompt_preparation(i18n=center.i18n, force_rebuild=True)
        snapshot = prompt_preparation.snapshot()
        self.assertIsInstance(prompt_preparation, PromptPreparationBundle)
        self.assertEqual(snapshot["class"], "PromptPreparationBundle")
        self.assertEqual(snapshot["command_rotator"], "verdreheWoReTaBefehl")
        self.assertEqual(snapshot["regex_rewriter"], "regExReplace")
        self.assertEqual(snapshot["output_preparer"], "promptVorbereitungGrosseAusgabe")
        self.assertGreaterEqual(snapshot["beenden_commands_len"], 1)
        text_state = self.architecture.bootstrap_prompt_session(i18n=center.i18n).new_text_state("reta -spalten --religionen=sternpolygon")
        self.assertEqual(prompt_preparation.regex_replace(text_state), text_state.liste)

    def test_prompt_interaction_layer_is_explicit(self):
        prompt_interaction = self.architecture.bootstrap_prompt_interaction(i18n=center.i18n, force_rebuild=True)
        snapshot = prompt_interaction.snapshot()
        self.assertIsInstance(prompt_interaction, PromptInteractionBundle)
        self.assertEqual(snapshot["class"], "PromptInteractionBundle")
        self.assertEqual(snapshot["session_layer"], "PromptSessionBundle")
        self.assertEqual(snapshot["preparation_layer"], "PromptPreparationBundle")
        self.assertEqual(snapshot["execution_layer"], "PromptExecutionBundle")
        self.assertFalse(snapshot["has_nested_completer"])
        self.assertGreater(snapshot["befehle_len"], 100)

    def test_completion_runtime_layer_is_explicit(self):
        completion_runtime = self.architecture.bootstrap_completion_runtime(i18n=center.i18n, force_rebuild=True)
        snapshot = completion_runtime.snapshot()
        self.assertEqual(snapshot["befehle_len"], len(LibRetaPrompt.completionRuntime.befehle))
        self.assertEqual(
            sorted(snapshot["kombi_option_keys"]),
            ["*", center.i18n.kombiMainParas["galaxie"], center.i18n.kombiMainParas["universum"]],
        )
        self.assertIn("15_", completion_runtime.start_commands(include_numeric_shortcuts=True))
        self.assertEqual(completion_runtime.program.paraDict, LibRetaPrompt.completionRuntime.program.paraDict)

    def test_prompt_language_layer_is_explicit(self):
        prompt_language = self.architecture.bootstrap_prompt_language(i18n=center.i18n, force_rebuild=True)
        snapshot = prompt_language.snapshot()
        self.assertEqual(snapshot["class"], "PromptLanguageBundle")
        self.assertEqual(snapshot["not_parameter_values_len"], len(LibRetaPrompt.notParameterValues))
        self.assertEqual(snapshot["gebrochen_erlaubte_zahlen_len"], len(LibRetaPrompt.gebrochenErlaubteZahlen))
        self.assertEqual(prompt_language.wahl15, LibRetaPrompt.wahl15)
        self.assertTrue(isReTaParameter("--religionen=sternpolygon"))
        self.assertTrue(is15or16command("15_"))
        self.assertEqual(custom_split("alpha (beta gamma) delta"), ["alpha", "(beta gamma)", "delta"])
        self.assertEqual(custom_split2("{1,2},3", ","), ["{1,2}", "3"])
        self.assertEqual(verkuerze_dict({"a": 1, "b": 1, "c": 2}), {"a": 1, "c": 2})
        self.assertEqual(
            verifyBruchNganzZahlBetweenCommas([], "", [], [], [], "5", []),
            ([True], [], [], ["5"], True),
        )
        if_kurz, expanded = stextFromKleinKleinKleinBefehl(PromptModus.normal, ["p5"], [])
        self.assertTrue(if_kurz)
        self.assertEqual(expanded, [center.i18n.befehle2["mulpri"], "5"])

    def test_center_uses_split_i18n_proxy(self):
        self.assertEqual(
            center.i18n.__source_modules__,
            ("i18n.words_context", "i18n.words_matrix", "i18n.words_runtime"),
        )
        self.assertEqual(center.ROW_RANGE_SYNTAX.multiple_prefix, center.i18n.befehle2["v"])
        self.assertEqual(center.BereichToNumbers2("1-3"), {1, 2, 3})
        self.assertEqual(center.BereichToNumbers2(f"{center.i18n.befehle2['v']}2-2", False, 7), {2, 4, 6})

    def test_prompt_vocabulary_matches_exported_globals(self):
        vocabulary = LibRetaPrompt.promptVocabulary
        self.assertEqual(LibRetaPrompt.mainParas, list(vocabulary.main_parameters))
        self.assertEqual(LibRetaPrompt.ausgabeParas, list(vocabulary.ausgabe_paras))
        self.assertEqual(LibRetaPrompt.kombiMainParas, list(vocabulary.kombi_main_paras))
        self.assertEqual(LibRetaPrompt.zeilenParas, list(vocabulary.zeilen_paras))
        self.assertEqual(LibRetaPrompt.hauptForNebenSet, set(vocabulary.haupt_for_neben_set))
        self.assertEqual(LibRetaPrompt.gebrochenErlaubteZahlen, set(vocabulary.gebrochen_erlaubte_zahlen))
        self.assertEqual(LibRetaPrompt.befehle2, set(vocabulary.befehle2))

    def test_libretaprompt_is_thin_compatibility_facade(self):
        source = (REPO_ROOT / "libs" / "LibRetaPrompt.py").read_text(encoding="utf-8")
        self.assertIn("bootstrap_prompt_runtime", source)
        self.assertIn("bootstrap_prompt_language", source)
        self.assertIn("bootstrap_prompt_session", source)
        self.assertNotIn("reta.Program([sys.argv[0]", source)
        self.assertNotIn("class PromptModus", source)
        self.assertNotIn("def custom_split", source)
        self.assertNotIn("def stextFromKleinKleinKleinBefehl", source)
        self.assertEqual(type(LibRetaPrompt.retaProgram).__name__, "PromptProgramView")
        self.assertEqual(type(LibRetaPrompt.promptSession).__name__, "PromptSessionBundle")
        self.assertNotIsInstance(LibRetaPrompt.retaProgram, reta.Program)


    def test_completion_stack_sources_use_explicit_completion_runtime(self):
        nested_source = (REPO_ROOT / "libs" / "nestedAlx.py").read_text(encoding="utf-8")
        reta_prompt_source = (REPO_ROOT / "retaPrompt.py").read_text(encoding="utf-8")
        nested_tree = ast.parse(nested_source)
        reta_prompt_tree = ast.parse(reta_prompt_source)

        def collect_imports(tree):
            imports = {}
            for node in tree.body:
                if isinstance(node, ast.ImportFrom):
                    imports.setdefault(node.module, set()).update(alias.name for alias in node.names)
            return imports

        nested_imports = collect_imports(nested_tree)
        reta_prompt_imports = collect_imports(reta_prompt_tree)

        self.assertEqual(set(nested_imports.get("LibRetaPrompt", set())), {"completionRuntime"})
        self.assertEqual(
            set(nested_imports.get("reta_architecture", set())),
            {"PromptModus", "stextFromKleinKleinKleinBefehl"},
        )
        self.assertEqual(
            set(reta_prompt_imports.get("nestedAlx", set())),
            {"ComplSitua", "NestedCompleter"},
        )
        self.assertEqual(
            set(reta_prompt_imports.get("reta_architecture", set())),
            {"PromptModus", "PromptTextState"},
        )
        self.assertEqual(
            set(reta_prompt_imports.get("reta_architecture.prompt_interaction", set())),
            {"PromptInteractionBundle", "bootstrap_prompt_interaction"},
        )
        self.assertIn("promptInteraction = bootstrap_prompt_interaction", reta_prompt_source)
        self.assertIn("promptInteraction.run_scope", reta_prompt_source)
        self.assertIn("promptInteraction.prompt_input", reta_prompt_source)
        self.assertIn("promptInteraction.store_prompt", reta_prompt_source)
        self.assertIn("promptInteraction.delete_before_storage_commands", reta_prompt_source)
        self.assertNotIn("promptSession.build_loop_setup", reta_prompt_source)
        self.assertNotIn("promptExecution.run_grosse_ausgabe", reta_prompt_source)
        self.assertNotIn("promptPreparation.prepare_grosse_ausgabe", reta_prompt_source)
        self.assertNotIn("def PromptGrosseAusgabe", reta_prompt_source)
        self.assertNotIn("def bruchBereichsManagementAndWbefehl", reta_prompt_source)
        self.assertNotIn("def regExReplace", reta_prompt_source)
        self.assertNotIn("def promptVorbereitungGrosseAusgabe", reta_prompt_source)
        self.assertNotIn("class TXT", reta_prompt_source)


    def test_column_selection_layer_is_explicit(self):
        column_selection = self.architecture.bootstrap_column_selection()
        snapshot = column_selection.snapshot()
        self.assertEqual(snapshot["class"], "ColumnSelectionBundle")
        self.assertEqual(snapshot["positive_bucket_count"], 12)
        self.assertEqual(snapshot["negative_bucket_count"], 12)
        self.assertEqual(column_selection.type_naming.ordinary, (0, 0))
        self.assertEqual(column_selection.type_naming.metakonkretNot, (1, 11))
        bucket_map = column_selection.new_bucket_map()
        self.assertEqual(sorted(bucket_map.keys()), [(neg, bucket) for neg in (0, 1) for bucket in range(12)])

    def test_generated_columns_layer_is_explicit(self):
        generated_columns = self.architecture.bootstrap_generated_columns(force_rebuild=True)
        snapshot = generated_columns.snapshot()
        self.assertIsInstance(generated_columns, GeneratedColumnsBundle)
        self.assertEqual(snapshot["class"], "GeneratedColumnsBundle")
        self.assertGreaterEqual(snapshot["count"], 9)
        names = [item["method_name"] for item in snapshot["morphisms"]]
        self.assertIn("concatLovePolygon", names)
        self.assertIn("concatVervielfacheZeile", names)
        self.assertIn("concatModallogik", names)
        self.assertIn("concat1RowPrimUniverse2", names)
        self.assertIn("concat1PrimzahlkreuzProContra", names)
        self.assertIn("concatPrimCreativityType", names)
        self.assertIn("concatGleichheitFreiheitDominieren", names)
        self.assertIn("concatGeistEmotionEnergieMaterieTopologie", names)
        self.assertIn("concatMondExponzierenLogarithmusTyp", names)
        self.assertIn("generated_columns", self.architecture.snapshot())
        self.assertIn("generated_columns_registry", self.architecture.bootstrap_table_generation().snapshot())

    def test_table_output_layer_is_explicit(self):
        table_output = self.architecture.bootstrap_table_output(force_rebuild=True)
        snapshot = table_output.snapshot()
        self.assertIsInstance(table_output, TableOutputBundle)
        self.assertEqual(snapshot["class"], "TableOutputBundle")
        self.assertEqual(snapshot["output_class"], "TableOutput")
        tables = __import__("tableHandling").Tables(None, [])
        renderer = table_output.create(tables, [])
        self.assertEqual(type(renderer).__name__, "TableOutput")
        self.assertIs(renderer.tables, tables)


    def test_row_filtering_layer_is_explicit(self):
        row_filtering = self.architecture.bootstrap_row_filtering()
        snapshot = row_filtering.snapshot()
        self.assertIsInstance(row_filtering, RowFilteringBundle)
        self.assertEqual(snapshot["class"], "RowFilteringBundle")
        self.assertEqual(snapshot["legacy_owner"], "libs.lib4tables_prepare.Prepare")
        self.assertIn("moon_sun_planet", snapshot["condition_families"])
        self.assertIn("z_y_position_filters", snapshot["condition_families"])
        self.assertIn("row_filtering", self.architecture.snapshot())

    def test_table_wrapping_layer_is_explicit(self):
        table_wrapping = self.architecture.bootstrap_table_wrapping(force_rebuild=True)
        snapshot = table_wrapping.snapshot()
        self.assertIsInstance(table_wrapping, TableWrappingBundle)
        self.assertEqual(snapshot["class"], "TableWrappingBundle")
        self.assertEqual(snapshot["legacy_owner"], "libs.lib4tables_prepare.Prepare")
        self.assertIn("wrap_cell_text", snapshot["morphisms"])
        self.assertIn("width_for_row", snapshot["morphisms"])
        self.assertIn("table_wrapping", self.architecture.snapshot())

    def test_number_theory_layer_is_explicit(self):
        number_theory = self.architecture.bootstrap_number_theory()
        snapshot = number_theory.snapshot()
        self.assertIsInstance(number_theory, NumberTheoryBundle)
        self.assertEqual(snapshot["class"], "NumberTheoryBundle")
        self.assertEqual(snapshot["dependency_profile"], "math-only")
        self.assertIn("primCreativity", snapshot["morphisms"])
        self.assertIn("moonNumber", snapshot["morphisms"])
        self.assertEqual(arch_prim_creativity(1), lib4tables.primCreativity(1))
        self.assertEqual(arch_prim_creativity(12), lib4tables.primCreativity(12))
        self.assertEqual(arch_moon_number(16), lib4tables.moonNumber(16))
        self.assertIn("number_theory", self.architecture.snapshot())

    def test_prepare_stack_delegates_to_row_filtering_layer(self):
        prepare_source = (REPO_ROOT / "libs" / "lib4tables_prepare.py").read_text(encoding="utf-8")
        row_filtering_source = (REPO_ROOT / "reta_architecture" / "row_filtering.py").read_text(encoding="utf-8")
        self.assertIn("architecture_filter_original_lines", prepare_source)
        self.assertIn("architecture_parameters_cmd_with_some_bereich", prepare_source)
        self.assertIn("architecture_set_zaehlungen", prepare_source)
        self.assertIn("def filter_original_lines", row_filtering_source)
        self.assertIn("def parameters_cmd_with_some_bereich", row_filtering_source)
        self.assertIn("def set_zaehlungen", row_filtering_source)
        self.assertIn("from .number_theory import isPrimMultiple, moonNumber, primFak", row_filtering_source)
        self.assertNotIn("from lib4tables import isPrimMultiple", row_filtering_source)
        self.assertLess(prepare_source.count('if "mond" in condition'), row_filtering_source.count('if "mond" in condition'))

    def test_table_preparation_layer_is_explicit(self):
        table_preparation = self.architecture.bootstrap_table_preparation()
        snapshot = table_preparation.snapshot()
        self.assertIsInstance(table_preparation, TablePreparationBundle)
        self.assertEqual(snapshot["class"], "TablePreparationBundle")
        self.assertEqual(snapshot["display_line_morphism"], "select_display_lines")
        self.assertEqual(snapshot["tag_gluing_morphism"], "tag_output_column")
        self.assertIn("prepare_main_output", snapshot["universal_operations"])
        self.assertIn("prepare_kombi_output", snapshot["universal_operations"])
        self.assertIn("table_preparation", self.architecture.snapshot())

    def test_table_generation_layer_is_explicit(self):
        table_generation = self.architecture.bootstrap_table_generation(csv_file_names=center.i18n.csvFileNames)
        snapshot = table_generation.snapshot()
        self.assertEqual(snapshot["class"], "TableGenerationBundle")
        self.assertIn("concatModallogik", snapshot["generated_morphisms"])
        self.assertIn("concat1RowPrimUniverse2", snapshot["generated_morphisms"])
        self.assertIn("concat1PrimzahlkreuzProContra", snapshot["generated_morphisms"])
        self.assertIn("createSpalteGestirn", snapshot["generated_morphisms"])
        self.assertEqual(len(snapshot["kombi_csvs"]), 2)


    def test_parameter_runtime_layer_is_explicit(self):
        parameter_runtime = self.architecture.bootstrap_parameter_runtime()
        snapshot = parameter_runtime.snapshot()
        self.assertIsInstance(parameter_runtime, ParameterRuntimeBundle)
        self.assertEqual(snapshot["class"], "ParameterRuntimeBundle")
        self.assertEqual(snapshot["column_function"], "produce_all_spalten_numbers")
        self.assertEqual(snapshot["parse_function"], "parameters_to_commands_and_numbers")
        self.assertEqual(snapshot["upper_limit_apply_function"], "apply_upper_limit_argument")
        self.assertIn("parameter_runtime", self.architecture.snapshot())

    def test_program_workflow_layer_is_explicit(self):
        program_workflow = self.architecture.bootstrap_program_workflow()
        snapshot = program_workflow.snapshot()
        self.assertIsInstance(program_workflow, ProgramWorkflowBundle)
        self.assertEqual(snapshot["class"], "ProgramWorkflowBundle")
        self.assertIn("load_religion_table", snapshot["orchestration_steps"])
        self.assertIn("join_kombi_tables", snapshot["orchestration_steps"])
        self.assertEqual(len(snapshot["kombi_csvs"]), 2)
        self.assertIn("program_workflow", self.architecture.snapshot())

    def test_prepare_stack_delegates_to_table_preparation_layer(self):
        prepare_source = (REPO_ROOT / "libs" / "lib4tables_prepare.py").read_text(encoding="utf-8")
        program_workflow_source = (REPO_ROOT / "reta_architecture" / "program_workflow.py").read_text(encoding="utf-8")
        table_generation_source = (REPO_ROOT / "reta_architecture" / "table_generation.py").read_text(encoding="utf-8")
        table_preparation_source = (REPO_ROOT / "reta_architecture" / "table_preparation.py").read_text(encoding="utf-8")
        self.assertIn("architecture_prepare_output_table", prepare_source)
        self.assertIn("architecture_select_display_lines", prepare_source)
        self.assertIn("architecture_tag_output_column", prepare_source)
        self.assertIn("prepare_main_output", program_workflow_source)
        self.assertIn("prepare_kombi_output", program_workflow_source)
        self.assertIn("capture_last_line_number", table_generation_source)
        self.assertIn("def prepare_output_table", table_preparation_source)
        self.assertIn("def tag_output_column", table_preparation_source)
        self.assertLess(prepare_source.count("lib4tables_Enum.tableTags2"), table_preparation_source.count("lib4tables_Enum.tableTags2"))

    def test_reta_program_delegates_to_program_workflow_layer(self):
        reta_source = (REPO_ROOT / "reta.py").read_text(encoding="utf-8")
        workflow_source = (REPO_ROOT / "reta_architecture" / "program_workflow.py").read_text(encoding="utf-8")
        self.assertIn("bootstrap_program_workflow", reta_source)
        self.assertIn("workflow_everything", reta_source)
        self.assertIn("combi_table_workflow", reta_source)
        self.assertIn("bootstrap_column_selection", workflow_source)
        self.assertIn("bind_program_sections", workflow_source)
        self.assertIn("bootstrap_table_generation", workflow_source)
        self.assertIn("build_for_program", workflow_source)
        self.assertIn("parameters_to_commands_and_numbers", reta_source)
        self.assertIn("produce_all_spalten_numbers", reta_source)
        self.assertNotIn("def resultingSpaltenFromTuple", reta_source)
        self.assertNotIn("def parameters_to_commands_and_numbers", reta_source)
        self.assertNotIn("CsvTheirsSpalten: dict = {}", reta_source)
        self.assertNotIn("namedtuple(\n            \"SpaltenTyp\"", reta_source)


    def test_output_syntax_layer_is_explicit(self):
        output_syntax = self.architecture.bootstrap_output_syntax(force_rebuild=True)
        snapshot = output_syntax.snapshot()
        self.assertIsInstance(output_syntax, OutputSyntaxBundle)
        self.assertEqual(snapshot["class"], "OutputSyntaxBundle")
        self.assertEqual(snapshot["architecture_owner"], "reta_architecture.output_syntax")
        self.assertIn("html", snapshot["modes"])
        self.assertTrue(snapshot["modes"]["markdown"]["force_zero_width"])
        self.assertIs(output_syntax.class_for("markdown"), lib4tables.markdownSyntax)
        self.assertIn("output_syntax", self.architecture.snapshot())

    def test_lib4tables_is_thin_number_and_output_facade(self):
        lib4tables_source = (REPO_ROOT / "libs" / "lib4tables.py").read_text(encoding="utf-8")
        output_syntax_source = (REPO_ROOT / "reta_architecture" / "output_syntax.py").read_text(encoding="utf-8")
        self.assertIn("reta_architecture.output_syntax", lib4tables_source)
        self.assertIn("reta_architecture.number_theory", lib4tables_source)
        self.assertNotIn("class htmlSyntax", lib4tables_source)
        self.assertNotIn("def primFak", lib4tables_source)
        self.assertIn("class htmlSyntax", output_syntax_source)
        self.assertIn("class OutputSyntaxBundle", output_syntax_source)

    def test_output_semantics_is_explicit(self):
        snapshot = self.architecture.snapshot()["output_semantics"]
        self.assertEqual(snapshot["available_modes"], ["bbcode", "csv", "emacs", "html", "markdown", "nichts", "shell"])
        self.assertTrue(snapshot["mode_specs"]["csv"]["force_one_table"])
        self.assertTrue(snapshot["mode_specs"]["markdown"]["force_zero_width"])

    def test_output_mode_registry_matches_table_runtime(self):
        program = self._build_program()
        self.assertEqual(program.architecture.output_semantics.mode_for_tables(program.tables), "shell")
        application = program.apply_output_mode("markdown")
        self.assertTrue(application)
        self.assertEqual(program.tables.outputModeName, "markdown")
        self.assertTrue(program.tables.markdownOutputYes)
        self.assertIsInstance(program.tables.outType, lib4tables.markdownSyntax)
        program.apply_output_mode("html")
        self.assertEqual(program.tables.outputModeName, "html")
        self.assertTrue(program.tables.htmlOutputYes)

    def test_semantic_builder_does_not_mutate_schema_sets(self):
        source = (REPO_ROOT / "reta_architecture" / "semantics_builder.py").read_text(encoding="utf-8")
        self.assertIn("next(iter(spalten_nummer_oder_etc))", source)
        self.assertNotIn("spalten_nummer_oder_etc.pop()", source)

    def test_empty_modal_concat_short_circuits(self):
        source = (REPO_ROOT / "reta_architecture" / "generated_columns.py").read_text(encoding="utf-8")
        concat_source = (REPO_ROOT / "libs" / "lib4tables_concat.py").read_text(encoding="utf-8")
        self.assertIn("def concat_modallogik", source)
        self.assertIn("if len(conceptsRowsSetOfTuple) == 0:", source)
        self.assertIn("return concat.relitable, rowsAsNumbers", source)
        self.assertIn("generated_column_morphisms.concat_modallogik", concat_source)
        self.assertIn("generated_column_morphisms.concat_vervielfache_zeile", concat_source)
        self.assertIn("generated_column_morphisms.concat_prim_universe_row", concat_source)
        self.assertIn("generated_column_morphisms.concat_primzahlkreuz_pro_contra", concat_source)

    def test_universal_merge_avoids_repeated_deepcopy(self):
        source = (REPO_ROOT / "reta_architecture" / "universal.py").read_text(encoding="utf-8")
        self.assertIn("merged_data_dicts = [dict(d) for d in data_dicts1]", source)
        self.assertIn("deepcopy every newly merged value", source)
        self.assertNotIn("deepcopy(dict(d))", source)

    def test_output_stack_sources_use_explicit_output_architecture(self):
        table_source = (REPO_ROOT / "libs" / "tableHandling.py").read_text(encoding="utf-8")
        table_runtime_source = (REPO_ROOT / "reta_architecture" / "table_runtime.py").read_text(encoding="utf-8")
        reta_source = (REPO_ROOT / "reta.py").read_text(encoding="utf-8")
        self.assertIn("from reta_architecture.table_runtime import", table_source)
        self.assertIn("OUTPUT_SEMANTICS = bootstrap_output_semantics", table_runtime_source)
        self.assertIn("from .table_output import TableOutput", table_runtime_source)
        self.assertNotIn("class Output:", table_runtime_source)
        self.assertIn("def apply_output_mode(self, outputtype: str)", reta_source)
        self.assertNotIn('if outputtype == i18n.ausgabeArt["shell"]', reta_source)

    def test_remaining_executable_scripts_use_split_i18n_proxy(self):
        html_source = (REPO_ROOT / "grundStrukHtml.py").read_text(encoding="utf-8")
        readme_source = (REPO_ROOT / "libs" / "generate4readme.py").read_text(encoding="utf-8")
        self.assertIn("build_split_i18n_proxy", html_source)
        self.assertIn("build_split_i18n_proxy", readme_source)
        self.assertNotIn("import i18n.words as i18n", html_source)
        self.assertNotIn("import i18n.words as i18n", readme_source)

    def test_package_integrity_manifest_is_explicit(self):
        manifest = RepoManifest.from_tree(REPO_ROOT)
        self.assertEqual(manifest.missing_required, ())
        self.assertGreaterEqual(manifest.file_count, 240)
        self.assertEqual(manifest.csv_line_counts["csv/religion.csv"], 1043)
        self.assertEqual(manifest.csv_line_counts["csv/vn-religion.csv"], 1043)
        self.assertEqual(manifest.suspicious_csvs, ())
        self.assertIn("reta_architecture/prompt_preparation.py", manifest.files)
        self.assertIn("reta_architecture/parameter_runtime.py", manifest.files)
        self.assertIn("reta_architecture/prompt_interaction.py", manifest.files)
        self.assertIn("reta_architecture/column_selection.py", manifest.files)
        self.assertIn("reta_architecture/table_generation.py", manifest.files)
        self.assertIn("reta_architecture/table_preparation.py", manifest.files)
        self.assertIn("reta_architecture/table_wrapping.py", manifest.files)
        self.assertIn("reta_architecture/table_state.py", manifest.files)
        self.assertIn("reta_architecture/table_output.py", manifest.files)
        self.assertIn("reta_architecture/table_runtime.py", manifest.files)
        self.assertIn("reta_architecture/output_syntax.py", manifest.files)
        self.assertIn("reta_architecture/program_workflow.py", manifest.files)
        self.assertIn("reta_architecture/concat_csv.py", manifest.files)
        self.assertIn("reta_architecture/combi_join.py", manifest.files)
        self.assertIn("reta_architecture/category_theory.py", manifest.files)
        self.assertIn("reta_architecture/architecture_map.py", manifest.files)
        self.assertIn("reta_architecture/architecture_contracts.py", manifest.files)
        self.assertIn("reta_architecture/architecture_witnesses.py", manifest.files)

    def test_parameter_semantics_regression_counts(self):
        program = self._semantic_program()
        self.assertEqual(len(program.paraDict), 4155)
        self.assertEqual(
            [len(d) if hasattr(d, "__len__") else None for d in program.dataDict],
            [554, 46, 11, 12, 7, 23, 23, 10, 14, 23, 23, 12, 0, 0],
        )
        self.assertEqual(len(program.kombiReverseDict), 46)
        self.assertEqual(len(program.kombiReverseDict2), 51)
        self.assertEqual(len(program.AllSimpleCommandSpalten), 554)

    def test_builder_standalone_matches_program_semantics(self):
        program = self._semantic_program()
        builder = ParameterSemanticsBuilder(
            self.architecture.schema,
            gebrochen_spalten_maximum_plus1=reta.gebrochenSpaltenMaximumPlus1,
            invert_alles=False,
            initial_data_dict=[{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}],
            prim_number_predicate=reta.primCreativity,
            alles_parameter_names=reta.i18n.ParametersMain.alles,
        )
        built = builder.build()
        self.assertEqual(len(built.para_dict), len(program.paraDict))
        self.assertEqual([len(d) for d in built.data_dict], [len(d) for d in program.dataDict])
        self.assertEqual(len(built.kombi_reverse_dict), len(program.kombiReverseDict))
        self.assertEqual(len(built.kombi_reverse_dict2), len(program.kombiReverseDict2))
        self.assertEqual(len(built.all_simple_command_columns), len(program.AllSimpleCommandSpalten))


    def test_meta_columns_layer_is_explicit(self):
        meta_columns = self.architecture.bootstrap_meta_columns(force_rebuild=True)
        snapshot = meta_columns.snapshot()
        self.assertIsInstance(meta_columns, MetaColumnsBundle)
        self.assertEqual(snapshot["class"], "MetaColumnsBundle")
        self.assertGreaterEqual(snapshot["count"], 3)
        names = {item["method_name"] for item in snapshot["morphisms"]}
        self.assertIn("spalteMetaKontretTheorieAbstrakt_etc_1", names)
        self.assertIn("spalteFuerGegenInnenAussenSeitlichPrim", names)
        self.assertIn("readOneCSVAndReturn", names)


    def test_concat_csv_layer_is_explicit(self):
        concat_csv = self.architecture.bootstrap_concat_csv(force_rebuild=True)
        snapshot = concat_csv.snapshot()
        self.assertIsInstance(concat_csv, ConcatCsvBundle)
        self.assertEqual(snapshot["class"], "ConcatCsvBundle")
        names = {item["method_name"] for item in snapshot["morphisms"]}
        self.assertIn("readConcatCsv", names)
        self.assertIn("readConcatCsv_SetHtmlParamaters", names)
        self.assertIn("convertFractionsToDictOfNumToPaareOfMulOfIntAndFraction", names)
        self.assertIn("concat_csv", self.architecture.snapshot())
        self.assertIn("prim", snapshot["csv_sources"])

    def test_concat_stack_delegates_to_concat_csv_layer(self):
        concat_source = (REPO_ROOT / "libs" / "lib4tables_concat.py").read_text(encoding="utf-8")
        concat_csv_source = (REPO_ROOT / "reta_architecture" / "concat_csv.py").read_text(encoding="utf-8")
        table_generation_source = (REPO_ROOT / "reta_architecture" / "table_generation.py").read_text(encoding="utf-8")
        self.assertIn("concat_csv_morphisms.readConcatCsv", concat_source)
        self.assertIn("concat_csv_morphisms.convertFractionsToDictOfNumToPaareOfMulOfIntAndFraction", concat_source)
        self.assertIn("def readConcatCsv", concat_csv_source)
        self.assertIn("def readConcatCsv_SetHtmlParamaters", concat_csv_source)
        self.assertIn("self.concat_csv.read_concat_csv", table_generation_source)
        self.assertNotIn("self.relitable, tableToAdd = self.tables.fillBoth", concat_source)
        self.assertIn("concat.relitable, tableToAdd = concat.tables.fillBoth", concat_csv_source)


    def test_combi_join_layer_is_explicit(self):
        combi_join = self.architecture.bootstrap_combi_join(force_rebuild=True)
        snapshot = combi_join.snapshot()
        self.assertIsInstance(combi_join, KombiJoinBundle)
        self.assertEqual(snapshot["class"], "KombiJoinBundle")
        self.assertIn("readKombiCsv", snapshot["morphisms"])
        self.assertIn("tableJoin", snapshot["morphisms"])
        self.assertIn("combi_join", self.architecture.snapshot())


    def test_table_state_layer_is_explicit(self):
        table_state = self.architecture.bootstrap_table_state(force_rebuild=True)
        snapshot = table_state.snapshot()
        self.assertIsInstance(table_state, TableStateBundle)
        self.assertEqual(snapshot["class"], "TableStateBundle")
        self.assertIn("generated_columns", snapshot["sections"])
        self.assertIn("table_state", self.architecture.snapshot())
        tables = self.architecture.bootstrap_table_runtime().create_tables(None, None)
        self.assertEqual(tables.tableStateSnapshot["highest_rows"], {1024: 1024, 114: 163})
        self.assertIs(tables.generatedSpaltenParameter, tables._state_sections.generated_columns.parameters)
        self.assertIs(tables.generatedSpaltenParameter_Tags, tables._state_sections.generated_columns.tags)
        tables.keineUeberschriften = True
        tables.keineleereninhalte = True
        tables.spaltegGestirn = True
        self.assertTrue(tables.tableStateSnapshot["display"]["keine_ueberschriften"])
        self.assertTrue(tables.tableStateSnapshot["display"]["keine_leeren_inhalte"])
        self.assertTrue(tables.tableStateSnapshot["display"]["spalte_gestirn"])

    def test_table_runtime_layer_owns_tables(self):
        table_source = (REPO_ROOT / "libs" / "tableHandling.py").read_text(encoding="utf-8")
        table_runtime_source = (REPO_ROOT / "reta_architecture" / "table_runtime.py").read_text(encoding="utf-8")
        reta_source = (REPO_ROOT / "reta.py").read_text(encoding="utf-8")
        generated_source = (REPO_ROOT / "reta_architecture" / "generated_columns.py").read_text(encoding="utf-8")
        combi_source = (REPO_ROOT / "reta_architecture" / "combi_join.py").read_text(encoding="utf-8")
        self.assertIn("from reta_architecture.table_runtime import", table_source)
        self.assertNotIn("class Tables:", table_source)
        self.assertIn("class Tables:", table_runtime_source)
        self.assertIn("from .table_state import TableStateBundle", table_runtime_source)
        self.assertNotIn("from reta_architecture.table_runtime import Tables", reta_source)
        self.assertIn("bootstrap_table_runtime().create_tables", reta_source)
        self.assertIn("state_sections", table_runtime_source)
        self.assertIn("from .combi_join import KombiJoin", table_runtime_source)
        self.assertIn("Combi = KombiJoin", table_runtime_source)
        self.assertNotIn("class Combi:", table_runtime_source)
        self.assertIn("table_runtime", self.architecture.snapshot())
        self.assertIn("def create_spalte_gestirn", generated_source)
        self.assertIn("createSpalteGestirn", generated_source)
        self.assertIn("class KombiJoin", combi_source)
        self.assertIn("def readKombiCsv", combi_source)
        self.assertIn("def tableJoin", combi_source)


    def test_category_theory_layer_is_explicit(self):
        category_theory = self.architecture.bootstrap_category_theory(force_rebuild=True)
        snapshot = category_theory.snapshot()
        self.assertIsInstance(category_theory, CategoryTheoryBundle)
        self.assertEqual(snapshot["class"], "CategoryTheoryBundle")
        self.assertIn("category_theory", self.architecture.snapshot())
        self.assertIn("natural_transformation", snapshot["paradigm"])
        self.assertGreaterEqual(snapshot["counts"]["categories"], 8)
        self.assertGreaterEqual(snapshot["counts"]["functors"], 12)
        self.assertGreaterEqual(snapshot["counts"]["natural_transformations"], 7)
        category_names = {item["name"] for item in snapshot["categories"]}
        self.assertIn("OpenRetaContextCategory", category_names)
        self.assertIn("TableSectionCategory", category_names)
        self.assertIn("LegacyFacadeCategory", category_names)
        functor_names = {item["name"] for item in snapshot["functors"]}
        self.assertIn("RawCommandPresheafFunctor", functor_names)
        self.assertIn("GeneratedColumnEndofunctorFamily", functor_names)
        self.assertIn("OutputRenderingFunctorFamily", functor_names)
        transformation_names = {item["name"] for item in snapshot["natural_transformations"]}
        self.assertIn("RawToCanonicalParameterTransformation", transformation_names)
        self.assertIn("PresheafToSheafGluingTransformation", transformation_names)
        self.assertIn("LegacyToArchitectureTransformation", transformation_names)
        self.assertIn("TableRuntimeToStateSectionsTransformation", transformation_names)
        self.assertEqual(snapshot["plan"]["behaviour_change"].split(";")[0], "keine beabsichtigte Laufzeit-/CLI-Verhaltensänderung")
        source = (REPO_ROOT / "reta_architecture" / "category_theory.py").read_text(encoding="utf-8")
        self.assertIn("class FunctorSpec", source)
        self.assertIn("class NaturalTransformationSpec", source)
        self.assertIn("bootstrap_category_theory", source)


    def test_architecture_map_layer_is_explicit(self):
        architecture_map = self.architecture.bootstrap_architecture_map(force_rebuild=True)
        snapshot = architecture_map.snapshot()
        self.assertIsInstance(architecture_map, ArchitectureMapBundle)
        self.assertEqual(snapshot["class"], "ArchitectureMapBundle")
        self.assertEqual(snapshot["stage"], 30)
        self.assertIn("architecture_map", self.architecture.snapshot())
        self.assertGreaterEqual(snapshot["counts"]["capsules"], 10)
        self.assertGreaterEqual(snapshot["counts"]["flows"], 10)
        self.assertGreaterEqual(snapshot["counts"]["legacy_mappings"], 10)
        self.assertEqual(snapshot["counts"]["stage_steps"], 30)
        capsule_names = {item["name"] for item in snapshot["capsules"]}
        self.assertIn("SchemaTopologyCapsule", capsule_names)
        self.assertIn("TableCoreCapsule", capsule_names)
        self.assertIn("CategoricalMetaCapsule", capsule_names)
        legacy_owners = {item["legacy_owner"] for item in snapshot["legacy_mappings"]}
        self.assertIn("reta.py", legacy_owners)
        self.assertIn("retaPrompt.py", legacy_owners)
        self.assertIn("libs/tableHandling.py", legacy_owners)
        self.assertIn("libs/lib4tables_concat.py", legacy_owners)
        self.assertIn("flowchart TD", snapshot["diagrams"]["mermaid"])
        self.assertIn("RetaArchitectureRoot", snapshot["diagrams"]["text"])
        self.assertEqual(snapshot["markdown_audit"]["markdown_files_in_stage27_package"], 58)
        self.assertEqual(snapshot["markdown_audit"]["uploaded_tar_markdown_files"], 0)
        source = (REPO_ROOT / "reta_architecture" / "architecture_map.py").read_text(encoding="utf-8")
        self.assertIn("ArchitectureWitnessBundle", snapshot["diagrams"]["text"])
        self.assertIn("class ArchitectureMapBundle", source)
        self.assertIn("bootstrap_architecture_map", source)


    def test_architecture_contract_layer_is_explicit(self):
        contracts = self.architecture.bootstrap_architecture_contracts(force_rebuild=True)
        snapshot = contracts.snapshot()
        self.assertIsInstance(contracts, ArchitectureContractsBundle)
        self.assertEqual(snapshot["class"], "ArchitectureContractsBundle")
        self.assertEqual(snapshot["stage"], 29)
        self.assertIn("architecture_contracts", self.architecture.snapshot())
        self.assertIn("commutative_diagram", snapshot["paradigm"])
        self.assertGreaterEqual(snapshot["counts"]["commutative_diagrams"], 8)
        self.assertGreaterEqual(snapshot["counts"]["capsule_contracts"], 10)
        self.assertGreaterEqual(snapshot["counts"]["laws"], 9)
        self.assertEqual(snapshot["validation"]["status"], "passed")
        diagram_names = {item["name"] for item in snapshot["commutative_diagrams"]}
        self.assertIn("RawCommandNaturalitySquare", diagram_names)
        self.assertIn("PresheafSheafGluingSquare", diagram_names)
        self.assertIn("RenderedOutputParitySquare", diagram_names)
        contract_names = {item["capsule"] for item in snapshot["capsule_contracts"]}
        self.assertIn("TableCoreCapsule", contract_names)
        self.assertIn("CategoricalMetaCapsule", contract_names)
        law_names = {item["name"] for item in snapshot["laws"]}
        self.assertIn("LegacyCompatibilityNaturalityLaw", law_names)
        self.assertIn("SheafGluingUniquenessLaw", law_names)
        self.assertIn("architecture_contracts.py", snapshot["plan"]["implemented_in_stage_29"][0])
        self.assertIn("ArchitectureContractsBundle", snapshot["diagrams"]["text"])
        source = (REPO_ROOT / "reta_architecture" / "architecture_contracts.py").read_text(encoding="utf-8")
        self.assertIn("class CommutativeDiagramSpec", source)
        self.assertIn("class CapsuleContractSpec", source)
        self.assertIn("class RefactorLawSpec", source)
        self.assertIn("bootstrap_architecture_contracts", source)


    def test_architecture_witness_layer_is_explicit(self):
        witnesses = self.architecture.bootstrap_architecture_witnesses(force_rebuild=True)
        snapshot = witnesses.snapshot()
        self.assertIsInstance(witnesses, ArchitectureWitnessBundle)
        self.assertEqual(snapshot["class"], "ArchitectureWitnessBundle")
        self.assertEqual(snapshot["stage"], 30)
        self.assertIn("architecture_witnesses", self.architecture.snapshot())
        self.assertIn("witness", snapshot["paradigm"])
        self.assertIn("proof_obligation", snapshot["paradigm"])
        self.assertGreaterEqual(snapshot["counts"]["capsule_slices"], 10)
        self.assertGreaterEqual(snapshot["counts"]["diagram_witnesses"], 8)
        self.assertGreaterEqual(snapshot["counts"]["naturality_witnesses"], 8)
        self.assertGreaterEqual(snapshot["counts"]["obligations"], 17)
        self.assertEqual(snapshot["validation"]["status"], "passed")
        self.assertEqual(snapshot["validation"]["missing_file_like_anchors"], [])
        slice_names = {item["capsule"] for item in snapshot["capsule_slices"]}
        self.assertIn("TableCoreCapsule", slice_names)
        self.assertIn("CategoricalMetaCapsule", slice_names)
        diagram_names = {item["diagram"] for item in snapshot["diagram_witnesses"]}
        self.assertIn("RawCommandNaturalitySquare", diagram_names)
        self.assertIn("LegacyArchitectureCompatibilitySquare", diagram_names)
        transformation_names = {item["transformation"] for item in snapshot["naturality_witnesses"]}
        self.assertIn("RawToCanonicalParameterTransformation", transformation_names)
        self.assertIn("ContractedNaturalityTransformation", transformation_names)
        self.assertIn("architecture_witnesses.py", snapshot["plan"]["implemented_in_stage_30"][0])
        self.assertIn("ArchitectureWitnessBundle", snapshot["diagrams"]["text"])
        source = (REPO_ROOT / "reta_architecture" / "architecture_witnesses.py").read_text(encoding="utf-8")
        self.assertIn("class ArchitectureWitnessBundle", source)
        self.assertIn("class AnchorWitnessSpec", source)
        self.assertIn("class CapsuleSliceSpec", source)
        self.assertIn("bootstrap_architecture_witnesses", source)


    def test_known_pair_lookup_still_resolves(self):
        pair = self.architecture.sheaves.parameter_semantics.canonicalize_pair(
            "Religionen", "Hinduismus"
        )
        self.assertEqual(pair, ("Religionen", "Hinduismus"))
        self.assertEqual(
            self.architecture.sheaves.parameter_semantics.column_numbers_for_pair(
                "Religionen", "Hinduismus"
            ),
            [217],
        )


if __name__ == "__main__":
    unittest.main()
