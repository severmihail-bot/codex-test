# legal-knowledge-library

`legal-knowledge-library` este un proiect pentru construirea unei biblioteci de cunoștințe juridice în Markdown, pornind de la documente sursă precum legi, hotărâri, norme, proceduri sau alte texte oficiale.

Scopul proiectului este să permită un workflow cloud în care:

1. documentele sursă sunt importate din Google Drive;
2. textele sunt normalizate într-un format ușor de procesat;
3. Codex web/cloud generează fișiere Markdown tematice în `knowledge/`;
4. fișierele sunt validate, revizuite și versionate în GitHub;
5. rezultatele pot fi exportate înapoi în Google Drive sau folosite ulterior într-un sistem de întrebări/răspunsuri.

## Principii

- Sursa de adevăr pentru lucru și review este repository-ul Git.
- Google Drive este folosit pentru importul documentelor și, ulterior, pentru exportul livrabilelor.
- Codex lucrează pe fișiere versionate, nu direct pe documente Google Drive.
- Conținutul juridic trebuie să fie susținut de citări explicite.
- Informațiile neclare se marchează cu `NECLAR`, nu se presupun.

## Structura proiectului

```text
sources/
  raw/          Documente brute, importate sau adăugate ca surse originale.
  normalized/   Versiuni text/Markdown curățate, pregătite pentru procesare.

knowledge/      Biblioteci Markdown generate pe baza surselor normalizate.

metadata/       Registre și metadate despre documente.

prompts/        Prompturi reutilizabile pentru Codex.

scripts/        Automatizări, import/export și validatoare.

docs/           Reguli de format, citare și tratare a incertitudinilor.

templates/      Modele reutilizabile pentru fișiere knowledge și metadate.
```

## Workflow țintă

```text
Google Drive
  ↓ import automat
sources/raw/
  ↓ normalizare
sources/normalized/
  ↓ Codex web/cloud
knowledge/
  ↓ validare + review
GitHub PR
  ↓ merge
export opțional în Google Drive
```


## Format knowledge library

Formatul fișierelor generate în `knowledge/` este documentat în:

- `docs/knowledge-format.md` — structură, frontmatter și reguli generale;
- `docs/citation-style.md` — stilul de citare pentru articole, alineate și secțiuni;
- `docs/uncertainty-policy.md` — modul de marcare a informațiilor neclare cu `NECLAR`.

Template-urile reutilizabile sunt în `templates/`:

- `templates/knowledge-file.md`;
- `templates/document-index.md`;
- `templates/document-registry-entry.yml`.



## Integrare Google Drive

Structura recomandată în Google Drive este:

```text
Legal Knowledge/
  Legal Sources/
  Legal Knowledge Export/
```

Configurarea folosește Workload Identity Federation pentru GitHub Actions, astfel încât nu este necesară o cheie JSON de service account. Detaliile sunt documentate în:

- `docs/google-drive-setup.md`;
- `docs/secrets.md`;
- `docs/workload-identity-federation.md`;
- `metadata/drive.yml`;
- `.env.example`;
- `docs/import-from-drive.md`.

## Validare automată

Proiectul include validatoare simple, fără dependențe externe:

```bash
python scripts/validate_metadata.py
python scripts/validate_knowledge.py
```

Aceste verificări rulează și în GitHub Actions prin `.github/workflows/validate.yml`.

## Stadiul curent

Acest repo conține fundația proiectului, formatul inițial pentru knowledge library, validatoare de bază și import manual din Google Drive pentru fișiere `.md` și `.txt`.

## Reguli pentru Codex

Instrucțiunile principale pentru Codex sunt în `AGENTS.md`. Pe scurt:

- nu inventa informații juridice;
- citează articolul, alineatul sau secțiunea relevantă;
- marchează informațiile ambigue cu `NECLAR`;
- nu modifica `sources/raw/` fără instrucțiune explicită;
- păstrează conținutul în română.
