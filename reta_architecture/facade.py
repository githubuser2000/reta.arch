from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from .input_semantics import InputBundle
from .column_selection import ColumnSelectionBundle, bootstrap_column_selection
from .output_semantics import RetaOutputSemantics, bootstrap_output_semantics
from .output_syntax import OutputSyntaxBundle, bootstrap_output_syntax
from .table_generation import bootstrap_table_generation
from .generated_columns import GeneratedColumnsBundle, bootstrap_generated_columns
from .meta_columns import MetaColumnsBundle, bootstrap_meta_columns
from .concat_csv import ConcatCsvBundle, bootstrap_concat_csv
from .combi_join import KombiJoinBundle, bootstrap_combi_join
from .table_preparation import TablePreparationBundle, bootstrap_table_preparation
from .table_wrapping import TableWrappingBundle, bootstrap_table_wrapping
from .table_state import TableStateBundle, bootstrap_table_state
from .parameter_runtime import ParameterRuntimeBundle, bootstrap_parameter_runtime
from .program_workflow import ProgramWorkflowBundle, bootstrap_program_workflow
from .number_theory import NumberTheoryBundle, bootstrap_number_theory
from .morphisms import MorphismBundle
from .presheaves import PresheafBundle
from .schema import RetaContextSchema
from .sheaves import SheafBundle
from .topology import ContextSelection, RetaContextTopology
from .universal import UniversalBundle


@dataclass
class RetaArchitecture:
    repo_root: Path
    schema: RetaContextSchema
    topology: RetaContextTopology
    inputs: InputBundle
    output_syntax: OutputSyntaxBundle
    output_semantics: RetaOutputSemantics
    presheaves: PresheafBundle
    sheaves: SheafBundle
    morphisms: MorphismBundle
    universal: UniversalBundle
    column_selection: ColumnSelectionBundle
    parameter_runtime: ParameterRuntimeBundle
    program_workflow: ProgramWorkflowBundle
    table_preparation: TablePreparationBundle
    table_wrapping: TableWrappingBundle
    table_state: TableStateBundle
    number_theory: NumberTheoryBundle
    table_output: TableOutputBundle
    table_runtime: object
    generated_columns: GeneratedColumnsBundle
    meta_columns: MetaColumnsBundle
    concat_csv: ConcatCsvBundle
    combi_join: KombiJoinBundle

    @classmethod
    def bootstrap(cls, repo_root: Optional[Path] = None) -> "RetaArchitecture":
        if repo_root is None:
            repo_root = Path(__file__).resolve().parent.parent
        repo_root = repo_root.resolve()

        import i18n.words as words  # compatibility facade / module split metadata
        import i18n.words_context as words_context
        import i18n.words_matrix as words_matrix
        import i18n.words_runtime as words_runtime
        from libs.lib4tables_Enum import ST, tableTags

        schema = RetaContextSchema.from_words_parts(
            context_module=words_context,
            matrix_module=words_matrix,
            runtime_module=words_runtime,
            tag_enum=ST,
            table_tags=tableTags,
        )
        schema.schema_modules.setdefault("compatibility", str(getattr(words, "__name__", "i18n.words")))
        if hasattr(words, "MODULE_SPLIT"):
            schema.schema_modules.update(
                {f"compat:{key}": value for key, value in dict(words.MODULE_SPLIT).items()}
            )

        topology = RetaContextTopology.from_schema(schema)
        inputs = InputBundle.from_schema(schema, i18n=words_runtime)
        output_syntax = bootstrap_output_syntax()
        output_semantics = bootstrap_output_semantics(repo_root)
        presheaves = PresheafBundle.discover(repo_root)
        sheaves = SheafBundle.from_repo(repo_root, schema)
        morphisms = MorphismBundle.from_topology_and_sheaves(topology, sheaves, output_semantics=output_semantics)
        universal = UniversalBundle(sheaves)
        column_selection = bootstrap_column_selection()
        parameter_runtime = bootstrap_parameter_runtime()
        table_preparation = bootstrap_table_preparation()
        table_wrapping = bootstrap_table_wrapping()
        table_state = bootstrap_table_state()
        number_theory = bootstrap_number_theory()
        from .table_output import bootstrap_table_output
        table_output = bootstrap_table_output()
        from .table_runtime import bootstrap_table_runtime
        table_runtime = bootstrap_table_runtime(output_semantics=output_semantics, table_state=table_state)
        generated_columns = bootstrap_generated_columns()
        meta_columns = bootstrap_meta_columns()
        concat_csv = bootstrap_concat_csv()
        combi_join = bootstrap_combi_join()
        program_workflow = bootstrap_program_workflow(
            repo_root=repo_root,
            i18n=words_runtime,
            csv_file_names=words_runtime.csvFileNames,
            gebrochen_spalten_maximum_plus1=words_runtime.gebrochenSpaltenMaximumPlus1,
        )
        return cls(
            repo_root=repo_root,
            schema=schema,
            topology=topology,
            inputs=inputs,
            output_syntax=output_syntax,
            output_semantics=output_semantics,
            presheaves=presheaves,
            sheaves=sheaves,
            morphisms=morphisms,
            universal=universal,
            column_selection=column_selection,
            parameter_runtime=parameter_runtime,
            program_workflow=program_workflow,
            table_preparation=table_preparation,
            table_wrapping=table_wrapping,
            table_state=table_state,
            number_theory=number_theory,
            table_output=table_output,
            table_runtime=table_runtime,
            generated_columns=generated_columns,
            meta_columns=meta_columns,
            concat_csv=concat_csv,
            combi_join=combi_join,
        )

    def sync_program_semantics(self, para_dict, data_dicts) -> None:
        self.sheaves.parameter_semantics.sync_program_semantics(para_dict, data_dicts)

    def sync_tables(self, tables, output_mode: Optional[str] = None, finally_display_lines=None, rows_range=None) -> None:
        resolved_output_mode = output_mode or self.output_semantics.mode_for_tables(tables)
        self.universal.sync_tables(
            tables,
            output_mode=resolved_output_mode,
            finally_display_lines=finally_display_lines,
            rows_range=rows_range,
        )

    def update_prompt_state(self, raw_text: str, tokens, context: Optional[ContextSelection] = None) -> None:
        self.presheaves.prompt_state.update(raw_text, tokens, context=context)


    def bootstrap_column_selection(self, ordered_set_factory=None, force_rebuild: bool = False):
        if ordered_set_factory is None and not force_rebuild:
            return self.column_selection
        return bootstrap_column_selection(ordered_set_factory=ordered_set_factory)

    def bootstrap_parameter_runtime(self, force_rebuild: bool = False):
        if not force_rebuild:
            return self.parameter_runtime
        return bootstrap_parameter_runtime()

    def bootstrap_program_workflow(self, csv_file_names=None, force_rebuild: bool = False):
        if csv_file_names is None and not force_rebuild:
            return self.program_workflow
        import i18n.words_runtime as words_runtime

        if csv_file_names is None:
            csv_file_names = words_runtime.csvFileNames
        return bootstrap_program_workflow(
            repo_root=self.repo_root,
            i18n=words_runtime,
            csv_file_names=csv_file_names,
            gebrochen_spalten_maximum_plus1=words_runtime.gebrochenSpaltenMaximumPlus1,
        )

    def bootstrap_table_preparation(self, force_rebuild: bool = False):
        if not force_rebuild:
            return self.table_preparation
        return bootstrap_table_preparation()

    def bootstrap_row_filtering(self, force_rebuild: bool = False):
        from .row_filtering import bootstrap_row_filtering

        return bootstrap_row_filtering()

    def bootstrap_table_state(self, force_rebuild: bool = False):
        if not force_rebuild:
            return self.table_state
        return bootstrap_table_state()

    def bootstrap_number_theory(self, force_rebuild: bool = False):
        if not force_rebuild:
            return self.number_theory
        return bootstrap_number_theory()

    def bootstrap_table_wrapping(self, force_rebuild: bool = False):
        if not force_rebuild:
            return self.table_wrapping
        return bootstrap_table_wrapping(force_refresh=True)

    def bootstrap_output_syntax(self, force_rebuild: bool = False):
        if not force_rebuild:
            return self.output_syntax
        return bootstrap_output_syntax()

    def bootstrap_table_output(self, force_rebuild: bool = False):
        if not force_rebuild:
            return self.table_output
        from .table_output import bootstrap_table_output
        return bootstrap_table_output()

    def bootstrap_table_runtime(self, force_rebuild: bool = False):
        if not force_rebuild:
            return self.table_runtime
        from .table_runtime import bootstrap_table_runtime
        return bootstrap_table_runtime(output_semantics=self.output_semantics, table_state=self.bootstrap_table_state())

    def bootstrap_generated_columns(self, force_rebuild: bool = False):
        if not force_rebuild:
            return self.generated_columns
        return bootstrap_generated_columns()

    def bootstrap_meta_columns(self, force_rebuild: bool = False):
        if not force_rebuild:
            return self.meta_columns
        return bootstrap_meta_columns()

    def bootstrap_concat_csv(self, force_rebuild: bool = False):
        if not force_rebuild:
            return self.concat_csv
        return bootstrap_concat_csv()

    def bootstrap_combi_join(self, force_rebuild: bool = False):
        if not force_rebuild:
            return self.combi_join
        return bootstrap_combi_join()

    def bootstrap_table_generation(self, csv_file_names=None, force_rebuild: bool = False):
        if csv_file_names is None:
            import i18n.words_runtime as words_runtime

            csv_file_names = words_runtime.csvFileNames
        return bootstrap_table_generation(
            csv_file_names=csv_file_names,
            generated_columns=self.bootstrap_generated_columns(),
            concat_csv=self.bootstrap_concat_csv(),
            combi_join=self.bootstrap_combi_join(),
        )

    def bootstrap_prompt_runtime(self, i18n=None, force_rebuild: bool = False):
        from .prompt_runtime import bootstrap_prompt_runtime

        return bootstrap_prompt_runtime(
            repo_root=self.repo_root,
            architecture=self,
            i18n=i18n,
            force_rebuild=force_rebuild,
        )


    def bootstrap_completion_runtime(self, i18n=None, force_rebuild: bool = False):
        from .completion_runtime import bootstrap_completion_runtime

        return bootstrap_completion_runtime(
            repo_root=self.repo_root,
            architecture=self,
            i18n=i18n,
            force_rebuild=force_rebuild,
        )

    def bootstrap_prompt_language(self, i18n=None, force_rebuild: bool = False):
        from .prompt_language import bootstrap_prompt_language

        return bootstrap_prompt_language(
            repo_root=self.repo_root,
            architecture=self,
            i18n=i18n,
            force_rebuild=force_rebuild,
        )

    def bootstrap_prompt_session(self, i18n=None, force_rebuild: bool = False):
        from .prompt_session import bootstrap_prompt_session

        return bootstrap_prompt_session(
            repo_root=self.repo_root,
            architecture=self,
            i18n=i18n,
            force_rebuild=force_rebuild,
        )

    def bootstrap_prompt_execution(self, i18n=None, force_rebuild: bool = False):
        from .prompt_execution import bootstrap_prompt_execution

        return bootstrap_prompt_execution(
            architecture=self,
            i18n=i18n,
            force_rebuild=force_rebuild,
        )

    def bootstrap_prompt_preparation(self, i18n=None, force_rebuild: bool = False):
        from .prompt_preparation import bootstrap_prompt_preparation

        return bootstrap_prompt_preparation(
            architecture=self,
            i18n=i18n,
            force_rebuild=force_rebuild,
        )

    def bootstrap_prompt_interaction(self, i18n=None, force_rebuild: bool = False, **kwargs):
        from .prompt_interaction import bootstrap_prompt_interaction

        return bootstrap_prompt_interaction(
            architecture=self,
            i18n=i18n,
            force_rebuild=force_rebuild,
            **kwargs,
        )

    def snapshot(self):
        return {
            "schema": self.schema.snapshot(),
            "topology": self.topology.snapshot(),
            "inputs": self.inputs.snapshot(),
            "output_syntax": self.bootstrap_output_syntax().snapshot(),
            "column_selection": self.bootstrap_column_selection().snapshot(),
            "parameter_runtime": self.bootstrap_parameter_runtime().snapshot(),
            "program_workflow": self.bootstrap_program_workflow().snapshot(),
            "table_generation": self.bootstrap_table_generation().snapshot(),
            "table_preparation": self.bootstrap_table_preparation().snapshot(),
            "row_filtering": self.bootstrap_row_filtering().snapshot(),
            "table_wrapping": self.bootstrap_table_wrapping().snapshot(),
            "table_state": self.bootstrap_table_state().snapshot(),
            "number_theory": self.bootstrap_number_theory().snapshot(),
            "table_output": self.bootstrap_table_output().snapshot(),
            "table_runtime": self.bootstrap_table_runtime().snapshot(),
            "generated_columns": self.bootstrap_generated_columns().snapshot(),
            "meta_columns": self.bootstrap_meta_columns().snapshot(),
            "concat_csv": self.bootstrap_concat_csv().snapshot(),
            "combi_join": self.bootstrap_combi_join().snapshot(),
            "output_semantics": self.output_semantics.snapshot(),
            "prompt_language": self.bootstrap_prompt_language().snapshot(),
            "prompt_session": self.bootstrap_prompt_session().snapshot(),
            "prompt_execution": self.bootstrap_prompt_execution().snapshot(),
            "prompt_preparation": self.bootstrap_prompt_preparation().snapshot(),
            "prompt_interaction": self.bootstrap_prompt_interaction().snapshot(),
            "presheaves": self.presheaves.snapshot(),
            "sheaves": self.sheaves.snapshot(),
            "morphisms": self.morphisms.snapshot(),
            "universal": self.universal.snapshot(),
        }
