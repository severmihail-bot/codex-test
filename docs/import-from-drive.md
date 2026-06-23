# Import din Google Drive

Importul din Google Drive este declanșat manual din GitHub Actions.

## Ce importă inițial

Scriptul importă doar fișiere din folderul `Legal Sources` cu extensiile:

```text
.md
.txt
```

Fișierele sunt salvate în:

```text
sources/raw/
```

Scriptul creează și un manifest:

```text
sources/raw/import-manifest.json
```

Manifestul păstrează ID-ul fișierului Drive, numele original, calea locală, tipul MIME și data modificării.

## Cum rulezi importul

În GitHub:

```text
Actions → Import from Google Drive → Run workflow
```

Workflow-ul va:

1. autentifica GitHub Actions în Google Cloud prin Workload Identity Federation;
2. instala dependențele Google Drive;
3. rula `scripts/import_from_drive.py`;
4. rula validatoarele existente;
5. crea un pull request cu fișierele importate.

## Secrets necesare

Importul folosește:

```text
GOOGLE_WORKLOAD_IDENTITY_PROVIDER
GOOGLE_SERVICE_ACCOUNT_EMAIL
GOOGLE_DRIVE_SOURCES_FOLDER_ID
```

Acestea trebuie configurate în GitHub Actions Secrets înainte de rulare.
