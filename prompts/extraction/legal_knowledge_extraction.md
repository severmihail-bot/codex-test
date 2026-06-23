# Extragere knowledge library juridică

Folosește acest prompt când generezi fișiere Markdown în `knowledge/` pe baza unui document din `sources/normalized/`.

## Instrucțiuni

1. Citește documentul sursă indicat de task.
2. Creează o structură flexibilă de fișiere în `knowledge/<document-id>/`, adaptată conținutului sursei, respectând `docs/knowledge-format.md`.
3. Preferă fișiere tematice, de exemplu: rezumat, definiții, domeniu de aplicare, obligații, termene, proceduri, sancțiuni, întrebări frecvente sau glosar, dacă aceste secțiuni sunt relevante pentru document.
4. Nu inventa informații juridice.
5. Orice afirmație juridică trebuie să citeze articolul, alineatul, punctul, litera sau secțiunea relevantă, conform `docs/citation-style.md`.
6. Dacă sursa nu este clară, marchează `NECLAR` folosind blocul standardizat din `docs/uncertainty-policy.md` și explică ce lipsește.
7. Include frontmatter YAML complet în fișierele generate, pornind de la `templates/knowledge-file.md` sau `templates/document-index.md`.

## Format recomandat pentru citări

```md
- Obligația X se aplică în condițiile Y. **Sursă:** Art. 12 alin. (3).
```
