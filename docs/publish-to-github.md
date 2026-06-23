# Publicarea schimbărilor în GitHub

Dacă repository-ul GitHub afișează doar commit-ul inițial și fișierul `.gitkeep`, înseamnă că schimbările pregătite în mediul Codex nu au fost publicate încă în GitHub.

## Situația curentă

Codex poate crea fișiere și commit-uri în mediul de lucru, dar acestea devin vizibile în GitHub doar după publicarea branch-ului sau după crearea unui Pull Request real în GitHub.

În GitHub trebuie să apară cel puțin aceste fișiere/directoare înainte de a rula importul:

```text
.github/workflows/import-drive.yml
.github/workflows/validate.yml
README.md
AGENTS.md
docs/
scripts/
metadata/
templates/
```

## Verificare rapidă în GitHub

În tabul **Code**, dacă vezi doar:

```text
.gitkeep
```

atunci repository-ul GitHub încă nu conține scaffold-ul proiectului.

## Ce trebuie făcut

Schimbările trebuie publicate din mediul Codex către repository-ul GitHub `severmihail-bot/codex-test`.

Dacă mediul Codex este conectat la GitHub, publicarea se face prin mecanismul de Pull Request al platformei.

Dacă mediul Codex nu este conectat la GitHub, utilizatorul trebuie fie să conecteze repository-ul la Codex web/cloud, fie să încarce/push-uiască schimbările printr-un mediu care are acces GitHub.

## După publicare

După ce fișierele apar în GitHub:

1. intră în tabul **Actions**;
2. selectează **Import from Google Drive**;
3. rulează workflow-ul manual;
4. verifică dacă fișierul din Google Drive apare în `sources/raw/`.
