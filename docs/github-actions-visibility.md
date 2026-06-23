# De ce nu apare workflow-ul în GitHub Actions

Dacă pagina **Actions** afișează mesajul „Get started with GitHub Actions”, repository-ul de pe GitHub nu vede încă niciun fișier de workflow în branch-ul curent.

## Cauza cea mai probabilă

Fișierele workflow există în repo-ul de lucru, dar nu au ajuns încă în repository-ul GitHub vizibil în browser.

Workflow-urile trebuie să existe în GitHub la calea:

```text
.github/workflows/
```

Pentru acest proiect, workflow-urile așteptate sunt:

```text
.github/workflows/import-drive.yml
.github/workflows/validate.yml
```

## Ce trebuie verificat în GitHub

1. Intră în tabul **Code** al repository-ului.
2. Verifică dacă există folderul `.github`.
3. Deschide `.github/workflows`.
4. Verifică dacă există `import-drive.yml` și `validate.yml`.

Dacă folderul `.github/workflows` nu există pe GitHub, atunci workflow-urile nu au fost încă publicate în acel repository/branch.

## Ce înseamnă pentru acest proiect

Codex poate crea fișierele workflow și le poate salva în git, dar pagina GitHub Actions le afișează doar după ce modificările sunt disponibile în repository-ul GitHub folosit de browser.

Dacă mediul Codex nu are remote GitHub configurat sau nu poate publica direct branch-ul, utilizatorul trebuie să se asigure că schimbările ajung în repository-ul GitHub înainte de a rula importul din Actions.

## Ce se face după ce apar workflow-urile

După ce `import-drive.yml` apare în GitHub:

1. intră în tabul **Actions**;
2. selectează **Import from Google Drive**;
3. apasă **Run workflow**;
4. verifică rezultatul rulării.
