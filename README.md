# Sito Antonio Cervigni

Generatore statico del sito antoniocervigni.it.

## Struttura

- `build2.py` — script generatore principale (legge `_source/Sito.dc.html` per il CSS di base, scrive l'output in `site/`)
- `icons.py`, `ritratti.py` — moduli con le icone SVG e i ritratti disegnati (Lacan, Dolto, Antonio)
- `art1.txt` – `art8.txt` — testi grezzi degli articoli della sezione "Scritti"
- `privacy_body.html` — testo della pagina privacy
- `_source/Sito.dc.html` — CSS di base esportato dal Design artifact
- `site/` — output generato (non versionato, vedi `.gitignore`)

## Come generare il sito

```bash
SITE_CONTACT_EMAIL='indirizzo@email.it' python3 -I build2.py
```

L'indirizzo email di contatto va passato come variabile d'ambiente al momento dell'esecuzione, non va mai scritto dentro i file del repository.

L'output completo viene scritto nella cartella `site/`.
