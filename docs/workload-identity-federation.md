# Workload Identity Federation pentru GitHub Actions

Acest proiect folosește Workload Identity Federation în locul unei chei JSON de service account.

## De ce

Dacă Google Cloud afișează mesajul `Service account key creation is disabled`, organizația blochează cheile JSON pentru service accounts. Aceasta este o restricție de securitate normală.

În această situație, GitHub Actions trebuie să se autentifice prin:

```text
GitHub Actions OIDC → Google Workload Identity Federation → service account
```

## Ce trebuie configurat în Google Cloud

1. Creează un Workload Identity Pool pentru GitHub Actions.
2. Creează un Workload Identity Provider în acel pool.
3. Configurează providerul pentru issuer-ul GitHub:

```text
https://token.actions.githubusercontent.com
```

4. Leagă providerul de repository-ul GitHub care va rula workflow-ul.
5. Acordă repository-ului dreptul de a impersona service account-ul creat pentru proiect.
6. Păstrează numele complet al providerului și email-ul service account-ului pentru GitHub Secrets.

## Secrets GitHub rezultate

La final, GitHub Actions are nevoie de:

```text
GOOGLE_WORKLOAD_IDENTITY_PROVIDER
GOOGLE_SERVICE_ACCOUNT_EMAIL
GOOGLE_DRIVE_SOURCES_FOLDER_ID
```

Pentru pașii ulteriori de export se vor folosi și:

```text
GOOGLE_DRIVE_ROOT_FOLDER_ID
GOOGLE_DRIVE_EXPORT_FOLDER_ID
```

## Formatul pentru provider

Valoarea `GOOGLE_WORKLOAD_IDENTITY_PROVIDER` arată aproximativ așa:

```text
projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/PROVIDER_ID
```

Nu este același lucru cu ID-ul proiectului. `PROJECT_NUMBER` este numărul numeric al proiectului Google Cloud.

## Permisiunea importantă

Service account-ul trebuie să permită providerului GitHub să îl impersonifice prin rolul:

```text
Workload Identity User
```

Fără această legătură, workflow-ul GitHub nu va putea obține credentiale Google temporare.
