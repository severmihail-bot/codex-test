# Politica pentru informații neclare

Knowledge library trebuie să favorizeze acuratețea în locul completitudinii aparente. Dacă o informație nu este susținută clar de sursă, nu trebuie inventată sau completată din presupuneri.

## Marker standard

Folosește blocul Markdown de avertizare:

```md
> [!WARNING]
> **NECLAR:** Explică aici ce informație lipsește sau ce ambiguitate există.
```

## Când se folosește `NECLAR`

Folosește `NECLAR` când:

- termenul aplicabil nu este precizat în sursă;
- categoria de persoane vizată nu este clară;
- există condiții sau excepții insuficient definite;
- sursa pare incompletă;
- documentul face trimitere la alt act normativ care nu este disponibil în repo;
- formularea sursei permite mai multe interpretări.

## Ce trebuie inclus într-un bloc `NECLAR`

Un bloc `NECLAR` trebuie să explice:

1. ce informație este neclară;
2. ce parte a sursei a generat incertitudinea;
3. ce ar trebui verificat la review uman.

## Exemplu

```md
> [!WARNING]
> **NECLAR:** Art. 15 menționează obligația de notificare, dar nu precizează termenul de transmitere. Este necesar review uman sau verificarea actelor normative la care articolul face trimitere.
```
