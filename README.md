# raspberry-debug

Erstimplementierung für ein leeres Repository: ein kleines CLI-Tool, das Raspberry-Pi-Logs auf häufige Fehlerbilder prüft.

## Features

- Erkennung von **Unterspannung**
- Erkennung von **SD-Karten-Timeouts**
- Erkennung von **Kernel Panic**
- Konsolenbericht mit Schweregrad und Handlungsempfehlung

## Nutzung

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
raspberry-debug /pfad/zum/syslog.txt
```

## Entwicklung

```bash
python -m pip install pytest
pytest
```
