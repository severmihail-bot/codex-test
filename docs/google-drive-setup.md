# Configurare Google Drive

Acest proiect folosește Google Drive pentru documente sursă și pentru exportul bibliotecii generate.

## Structură recomandată în Google Drive

Creează un folder părinte:

```text
Legal Knowledge
```

În el, creează două subfoldere:

```text
Legal Knowledge/
  Legal Sources/
  Legal Knowledge Export/
```

- `Legal Sources` va conține documentele de intrare.
- `Legal Knowledge Export` va conține fișierele Markdown generate sau exportate.

## Autentificare recomandată

Folosim un Google service account, dar fără cheie JSON în GitHub Actions.

Metoda recomandată este:

```text
GitHub Actions → Workload Identity Federation → service account → Google Drive API
```

Această metodă este potrivită când organizația Google blochează crearea cheilor JSON pentru service accounts.

## Pașii manuali

1. Creezi sau alegi un proiect Google Cloud.
2. Activezi Google Drive API.
3. Creezi un service account.
4. Configurezi Workload Identity Federation pentru GitHub Actions.
5. Acordezi providerului GitHub dreptul de a impersona service account-ul.
6. Partajezi folderul `Legal Knowledge` cu email-ul service account-ului.
7. Adaugi valorile necesare în GitHub Secrets.

## Secrets folosite de proiect

```text
GOOGLE_WORKLOAD_IDENTITY_PROVIDER
GOOGLE_SERVICE_ACCOUNT_EMAIL
GOOGLE_DRIVE_ROOT_FOLDER_ID
GOOGLE_DRIVE_SOURCES_FOLDER_ID
GOOGLE_DRIVE_EXPORT_FOLDER_ID
```

Aceste valori nu se commit-uiesc în repository.

## Tipuri de fișiere acceptate inițial

În prima etapă importăm doar fișiere simple:

```text
.md
.txt
```

Google Docs, `.docx` și `.pdf` vor fi adăugate într-o etapă ulterioară, după ce implementăm conversia și normalizarea.
