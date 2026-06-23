# Instrucțiuni pentru Codex

Acest repository conține o bibliotecă de cunoștințe juridice în Markdown. Scopul este să transformăm documente juridice sursă în fișiere `knowledge/` clare, verificabile și ușor de folosit ulterior pentru întrebări/răspunsuri.

## Limba proiectului

- Limba principală este româna.
- Documentația, prompturile și knowledge library trebuie scrise în română, cu excepția numelor tehnice de fișiere, variabile sau comenzi.

## Zonele principale ale repo-ului

- `sources/raw/` conține documente originale importate sau adăugate ca surse brute.
- `sources/normalized/` conține versiuni text/Markdown curățate ale surselor brute.
- `knowledge/` conține fișiere Markdown generate pe baza surselor normalizate.
- `metadata/` conține registre și metadate despre documente.
- `prompts/` conține instrucțiuni reutilizabile pentru task-uri Codex.
- `scripts/` conține automatizări și validatoare.

## Reguli obligatorii pentru conținut juridic

1. Nu inventa informații juridice.
2. Orice afirmație juridică trebuie să fie susținută prin citare la articol, alineat, punct, literă sau secțiune relevantă.
3. Dacă sursa nu susține clar o afirmație, marchează informația cu `NECLAR` și explică ce lipsește.
4. Nu transforma rezumatele în consultanță juridică finală.
5. Nu elimina excepții, condiții, termene sau limitări din sursă.
6. Păstrează diferența dintre textul legal, interpretare operațională și întrebări frecvente.

## Reguli pentru fișiere sursă

- Nu modifica fișierele din `sources/raw/` decât dacă task-ul cere explicit acest lucru.
- Folosește `sources/normalized/` ca sursă principală pentru generarea knowledge library.
- Dacă observi diferențe sau ambiguități între surse, oprește-te și marchează problema în răspuns sau într-un fișier de note.

## Reguli pentru knowledge library

- Structura fiecărei biblioteci de document poate fi flexibilă, adaptată documentului sursă.
- Preferă fișiere tematice scurte și clare în locul unui singur fișier foarte mare.
- Fiecare fișier Markdown din `knowledge/` trebuie să includă frontmatter YAML atunci când reprezintă conținut derivat dintr-o sursă juridică.
- Frontmatter recomandat:

```yaml
---
title: ""
source_document: ""
source_file: ""
status: "draft"
generated_by: "codex"
last_reviewed: ""
---
```

## Stil Markdown

- Folosește titluri clare.
- Folosește liste pentru obligații, termene, sancțiuni și condiții.
- Include citarea sursei lângă afirmația relevantă, nu doar la finalul fișierului.
- Marchează explicit secțiunile care necesită review uman.

## Verificări înainte de finalizarea unui task

- Verifică dacă fișierele create respectă structura repo-ului.
- Verifică dacă afirmațiile juridice importante au citări.
- Nu introduce secrete, tokenuri, parole sau credentiale reale în repo.
- Dacă există validatoare în `scripts/`, rulează-le înainte de finalizarea task-ului.

## Format standard knowledge library

- Respectă regulile din `docs/knowledge-format.md`, `docs/citation-style.md` și `docs/uncertainty-policy.md`.
- Folosește template-urile din `templates/` când creezi fișiere noi în `knowledge/`.
- Pentru citări, folosește formatul simplu în text: `**Sursă:** Art. X alin. (Y).`
- Pentru informații neclare, folosește blocul standardizat:

```md
> [!WARNING]
> **NECLAR:** Explică ce lipsește, unde apare ambiguitatea și ce trebuie verificat.
```
