# Secrets pentru GitHub Actions

Acest proiect citește configurarea sensibilă din GitHub Actions Secrets.

## Secrets necesare pentru importul din Google Drive

| Secret | Rol |
| --- | --- |
| `GOOGLE_WORKLOAD_IDENTITY_PROVIDER` | Numele complet al providerului Workload Identity Federation pentru GitHub Actions. |
| `GOOGLE_SERVICE_ACCOUNT_EMAIL` | Email-ul service account-ului impersonat de GitHub Actions. |
| `GOOGLE_DRIVE_ROOT_FOLDER_ID` | ID-ul folderului `Legal Knowledge`. |
| `GOOGLE_DRIVE_SOURCES_FOLDER_ID` | ID-ul folderului `Legal Sources`. |
| `GOOGLE_DRIVE_EXPORT_FOLDER_ID` | ID-ul folderului `Legal Knowledge Export`. |

## Unde se configurează

În GitHub:

```text
Repository → Settings → Secrets and variables → Actions → New repository secret
```

## De ce nu folosim cheia JSON ca metodă principală

Unele organizații Google blochează crearea cheilor JSON pentru service accounts prin politica `iam.disableServiceAccountKeyCreation`.

Pentru GitHub Actions, metoda recomandată în acest proiect este autentificarea fără cheie prin Workload Identity Federation. Astfel, GitHub Actions primește credentiale temporare și nu trebuie să stocăm o cheie JSON pe termen lung.

## Fallback local opțional

Scriptul `scripts/import_from_drive.py` mai poate citi `GOOGLE_SERVICE_ACCOUNT_JSON` pentru rulări locale, dar doar dacă organizația ta permite chei JSON. Nu folosi această variantă pentru GitHub Actions dacă Workload Identity Federation este disponibilă.

## Reguli

- Nu pune secrete reale în `.env.example`.
- Nu commit-ui chei JSON sau credentiale.
- Nu include tokenuri sau credentiale în prompturi Codex.
- Dacă un secret ajunge accidental în repo, trebuie revocat și regenerat.
