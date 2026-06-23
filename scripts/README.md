# Scripturi

Acest director va conține automatizări pentru proiect:

- `python scripts/import_from_drive.py` importă fișiere `.md` și `.txt` din Google Drive în `sources/raw/`;
- export în Google Drive;
- normalizarea documentelor;
- validarea knowledge library;
- verificarea citărilor.

Nu introduce secrete sau credentiale reale în acest director.


## Validatoare disponibile

- `python scripts/validate_metadata.py` verifică registrul `metadata/documents.yml`.
- `python scripts/validate_knowledge.py` verifică fișierele Markdown din `knowledge/`.

Aceste validatoare folosesc doar biblioteca standard Python, pentru a putea rula ușor în GitHub Actions și în mediile Codex cloud.
