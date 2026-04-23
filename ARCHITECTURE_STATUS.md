# Reta Architekturstatus (aktuell)
Stand: 2026-04-23

## Kurzfazit

Die mathematische Architektur ist implementiert, aktiviert und aktuell ohne
verbleibende Pflicht-Baustellen im Migrationsplan.

- Kategorien: **22**
- Funktoren: **62**
- natürliche Transformationen: **29**
- Stage-42-Fortschrittsoverlay: **30** beobachtete Surfaces,
  **34** Step-Progress-Einträge, **7** Wellen, **0** Outstanding-Items
- Wellenstatus: **M0–M6 alle `implemented_or_retained`**
- gemischte Owner: **keine mehr**
- Paketintegrität: **keine fehlenden Pflichtpfade**

## Seit der alten Restliste geschlossen

### 1. `libs/lib4tables_Enum.py`

Der frühere Misch-Owner ist geschlossen:

- das eigentliche Tag-/Enum-Schema lebt in `reta_architecture/tag_schema.py`
- `libs/lib4tables_Enum.py` ist nur noch Legacy-Kompatibilitätsfläche
- die Fortschrittsschicht klassifiziert die Datei nun als
  `extracted_to_compatibility_facade`

### 2. Paritätstest ohne externes Referenzarchiv

`tests/test_command_parity.py` ist nicht mehr auf
`/mnt/data/reta.todel.zip` angewiesen.

Die Suite arbeitet jetzt in dieser Reihenfolge:

1. externes Referenzarchiv verwenden, falls vorhanden
2. sonst per `git archive` aus einem Baseline-Commit ein temporäres
   Vergleichsarchiv erzeugen
3. optionalen Commit über `RETA_PARITY_BASELINE_COMMIT` respektieren

Damit ist der letzte echte Umgebungsblocker aus der alten Restliste im normalen
Repository-Checkout beseitigt.

## Zusätzlich bereinigt: keine Architektur-Rückimporte mehr in die Legacy-Fassaden

Die neue Architektur importiert ihre Runtime-Helfer jetzt nicht mehr aus
`libs/center.py`, `libs/lib4tables_prepare.py` oder
`libs/lib4tables_concat.py`. Stattdessen liegen die letzten Kompatibilitätsnamen
und Adapter innerhalb des Architekturpakets selbst:

- `reta_architecture/runtime_compat.py` bündelt i18n-, Range-, Arithmetik- und
  Console-Helfer architekturintern
- `reta_architecture/table_adapters.py` enthält die dünnen Architektur-Adapter
  für die früheren Klassen `Prepare` und `Concat`
- die betroffenen Architekturmodule (`row_filtering.py`, `prompt_execution.py`,
  `prompt_preparation.py`, `parameter_runtime.py`, `table_output.py`,
  `generated_columns.py`, `meta_columns.py`, `concat_csv.py`, `combi_join.py`,
  `table_wrapping.py`, `table_runtime.py`) greifen nur noch auf Architekturcode
  zu

Praktisch heißt das: Die neue Schicht hängt nicht mehr rückwärts an den alten
Wrapperdateien. Die Legacy-Dateien bleiben nur noch als optionale äußere
Kompatibilitätsoberfläche erhalten.

## Was jetzt noch bleibt

Nur noch optionale Nacharbeiten, keine Pflichtpunkte des Migrationsplans:

- `libs/center.py` weiter verdünnen
- `reta.py` weiter verdünnen
- `libs/lib4tables_prepare.py` weiter verdünnen
- `libs/lib4tables_concat.py` weiter verdünnen
- zusätzliche Paritätsfälle ergänzen
- optional eine versionierte Fixture zusätzlich zur Git-Baseline pflegen, falls
  Tests einmal in einem exportierten Tree ohne `.git` laufen sollen

Diese Punkte sind Optimierungen, keine strukturellen Architektur-Blocker.

## Validierungslage

Aktuell verifiziert:

- Architektur-Validierung: **51/51 Checks bestanden**
- Kohärenz: **passed**
- Rehearsal: **passed**
- Activation: **passed**
- Fortschrittsoverlay: **passed**
- Paketintegrität: **missing_required = []**

Zusätzlich erfolgreich ausgeführt:

- `python -m py_compile tests/test_command_parity.py tests/test_architecture_refactor.py reta_architecture/architecture_progress.py`
- `python -m unittest tests.test_command_parity.CommandParityMatrixTest.test_representative_command_matrix_matches_original -v`
- `python -m unittest tests.test_architecture_refactor.ArchitectureRefactorRegressionTest.test_architecture_progress_layer_is_explicit -v`

## Praktische Lesart

Die ursprüngliche Zielmenge — **Topologie, Morphismus, universelle
Eigenschaft, Prägarbe, Garbe, Kategorie, Funktor, natürliche Transformation** —
ist im Projekt nicht mehr bloß beschrieben, sondern in den aktiven
Architekturschichten verankert. Der Projektzustand ist deshalb nicht mehr
„Umbau läuft“, sondern **„Umbau abgeschlossen; verbleiben nur noch optionale
Nachverdichtungen“**.
