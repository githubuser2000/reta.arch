#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import json
import sys
from pathlib import Path


def _prepare_imports() -> Path:
    here = Path(__file__).resolve()
    candidates = [here.parent, here.parent.parent, Path.cwd()]
    for base in candidates:
        if (base / "i18n" / "words.py").exists():
            sys.path.insert(0, str(base))
            sys.path.insert(0, str(base / "libs"))
            return base
    raise SystemExit("Konnte reta-Repo nicht finden.")


REPO_ROOT = _prepare_imports()

from reta_architecture import RetaArchitecture  # noqa: E402
from reta_architecture.package_integrity import RepoManifest  # noqa: E402


ARCH = RetaArchitecture.bootstrap(REPO_ROOT)


def dump(value):
    print(json.dumps(value, ensure_ascii=False, separators=(",", ":")))


def help_text(program_name: str) -> str:
    return f"""{program_name} - Architektur-Inspektion für reta

Aufruf:
  {program_name} snapshot-json
  {program_name} schema-json
  {program_name} module-split-json
  {program_name} topology-json
  {program_name} inputs-json
  {program_name} column-selection-json
  {program_name} parameter-runtime-json
  {program_name} program-workflow-json
  {program_name} table-generation-json
  {program_name} table-preparation-json
  {program_name} row-filtering-json
  {program_name} table-wrapping-json
  {program_name} number-theory-json
  {program_name} table-output-json
  {program_name} table-runtime-json
  {program_name} generated-columns-json
  {program_name} meta-columns-json
  {program_name} concat-csv-json
  {program_name} combi-join-json
  {program_name} prompt-runtime-json
  {program_name} prompt-session-json
  {program_name} prompt-execution-json
  {program_name} prompt-preparation-json
  {program_name} prompt-interaction-json
  {program_name} package-integrity-json
  {program_name} completion-runtime-json
  {program_name} output-syntax-json
  {program_name} output-json
  {program_name} prompt-language-json
  {program_name} presheaves-json
  {program_name} sheaves-json
  {program_name} morphisms-json
  {program_name} universal-json
"""


def main(argv):
    program_name = Path(argv[0]).name if argv else "reta_architecture_probe_py.py"
    if len(argv) <= 1 or argv[1] in {"-h", "--help", "help"}:
        print(help_text(program_name))
        return 0
    cmd = argv[1]
    if cmd == "snapshot-json":
        dump(ARCH.snapshot())
        return 0
    if cmd == "schema-json":
        dump(ARCH.snapshot()["schema"])
        return 0
    if cmd == "module-split-json":
        dump(ARCH.snapshot()["schema"].get("schema_modules", {}))
        return 0
    if cmd == "topology-json":
        dump(ARCH.snapshot()["topology"])
        return 0
    if cmd == "inputs-json":
        dump(ARCH.snapshot()["inputs"])
        return 0
    if cmd == "column-selection-json":
        dump(ARCH.bootstrap_column_selection().snapshot())
        return 0
    if cmd == "parameter-runtime-json":
        dump(ARCH.bootstrap_parameter_runtime().snapshot())
        return 0
    if cmd == "program-workflow-json":
        dump(ARCH.bootstrap_program_workflow().snapshot())
        return 0
    if cmd == "table-generation-json":
        dump(ARCH.bootstrap_table_generation().snapshot())
        return 0
    if cmd == "table-preparation-json":
        dump(ARCH.bootstrap_table_preparation().snapshot())
        return 0
    if cmd == "row-filtering-json":
        dump(ARCH.bootstrap_row_filtering().snapshot())
        return 0
    if cmd == "table-wrapping-json":
        dump(ARCH.bootstrap_table_wrapping().snapshot())
        return 0
    if cmd == "number-theory-json":
        dump(ARCH.bootstrap_number_theory().snapshot())
        return 0
    if cmd == "table-output-json":
        dump(ARCH.bootstrap_table_output().snapshot())
        return 0
    if cmd == "table-runtime-json":
        dump(ARCH.bootstrap_table_runtime().snapshot())
        return 0
    if cmd == "generated-columns-json":
        dump(ARCH.bootstrap_generated_columns().snapshot())
        return 0
    if cmd == "meta-columns-json":
        dump(ARCH.bootstrap_meta_columns().snapshot())
        return 0
    if cmd == "concat-csv-json":
        dump(ARCH.bootstrap_concat_csv().snapshot())
        return 0
    if cmd == "combi-join-json":
        dump(ARCH.bootstrap_combi_join().snapshot())
        return 0
    if cmd == "prompt-runtime-json":
        dump(ARCH.bootstrap_prompt_runtime().snapshot())
        return 0
    if cmd == "completion-runtime-json":
        dump(ARCH.bootstrap_completion_runtime().snapshot())
        return 0
    if cmd == "prompt-session-json":
        dump(ARCH.bootstrap_prompt_session().snapshot())
        return 0
    if cmd == "prompt-execution-json":
        dump(ARCH.bootstrap_prompt_execution().snapshot())
        return 0
    if cmd == "prompt-preparation-json":
        dump(ARCH.bootstrap_prompt_preparation().snapshot())
        return 0
    if cmd == "prompt-interaction-json":
        dump(ARCH.bootstrap_prompt_interaction().snapshot())
        return 0
    if cmd == "package-integrity-json":
        dump(RepoManifest.from_tree(REPO_ROOT).snapshot())
        return 0
    if cmd == "output-syntax-json":
        dump(ARCH.bootstrap_output_syntax().snapshot())
        return 0
    if cmd == "output-json":
        dump(ARCH.snapshot()["output_semantics"])
        return 0
    if cmd == "prompt-language-json":
        dump(ARCH.bootstrap_prompt_language().snapshot())
        return 0
    if cmd == "presheaves-json":
        dump(ARCH.snapshot()["presheaves"])
        return 0
    if cmd == "sheaves-json":
        dump(ARCH.snapshot()["sheaves"])
        return 0
    if cmd == "morphisms-json":
        dump(ARCH.snapshot()["morphisms"])
        return 0
    if cmd == "universal-json":
        dump(ARCH.snapshot()["universal"])
        return 0
    raise SystemExit(f"Unbekannter Befehl: {cmd}")


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
