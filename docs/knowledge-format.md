# Formatul knowledge library

Acest document definește formatul standard pentru fișierele Markdown din `knowledge/`.

## Principii

- Structura unei biblioteci de document este flexibilă și se adaptează conținutului sursei.
- Formatul fiecărui fișier trebuie să fie consecvent, verificabil și ușor de citit.
- Fiecare afirmație juridică trebuie să aibă o citare lângă afirmația relevantă.
- Informațiile nesigure sau incomplete se marchează cu `NECLAR`.
- Fișierele generate sunt drafturi până la review uman.

## Structură recomandată pentru un document

Pentru un document juridic, Codex poate crea fișiere tematice precum:

```text
knowledge/<document-id>/
  index.md
  rezumat.md
  definitii.md
  domeniu-de-aplicare.md
  obligatii.md
  proceduri.md
  termene.md
  sanctiuni.md
  intrebari-frecvente.md
  glosar.md
```

Lista este orientativă. Codex poate adăuga, elimina sau redenumi fișierele dacă documentul sursă justifică acest lucru.

## Frontmatter obligatoriu pentru fișiere generate

Fiecare fișier Markdown generat în `knowledge/` trebuie să înceapă cu frontmatter YAML:

```yaml
---
title: ""
document_id: ""
source_document: ""
source_file: ""
source_type: ""
jurisdiction: "RO"
language: "ro"
status: "draft"
generated_by: "codex"
last_reviewed: ""
review_required: true
---
```

## Câmpuri frontmatter

- `title`: titlul fișierului sau al secțiunii tematice.
- `document_id`: identificator stabil pentru document, de exemplu `codul-fiscal`.
- `source_document`: numele documentului sursă.
- `source_file`: calea către fișierul din `sources/normalized/`.
- `source_type`: tipul documentului, de exemplu `lege`, `ordonanta`, `hotarare`, `norma`, `procedura`.
- `jurisdiction`: jurisdicția principală; implicit `RO`.
- `language`: limba conținutului; implicit `ro`.
- `status`: de regulă `draft`, până la review uman.
- `generated_by`: agentul sau procesul care a generat fișierul.
- `last_reviewed`: data ultimului review uman, dacă există.
- `review_required`: `true` până când conținutul este verificat.

## Secțiuni recomandate într-un fișier tematic

Un fișier tematic poate include:

```md
# Titlu

## Scop

## Reguli / informații extrase

## Excepții și condiții

## Zone neclare / necesită review
```

Nu toate secțiunile sunt obligatorii. Codex trebuie să păstreze doar secțiunile relevante pentru conținutul sursei.
