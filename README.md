# Passwort-Prüfer 🔐

Ein kleines Python-Programm, das prüft, wie sicher ein Passwort ist, und Tipps zur Verbesserung gibt.

> **Hinweis:** Dieses Projekt habe ich mit Unterstützung von KI (Claude Code) erstellt.
> Ich habe den Code durchgearbeitet, getestet und kann jeden Teil erklären.

## Was das Programm macht
- prüft Länge, Groß- und Kleinbuchstaben, Ziffern und Sonderzeichen
- erkennt sehr häufige Passwörter wie „123456“
- schätzt die Stärke in Bit (Entropie)
- versteckt die Eingabe, damit niemand mitlesen kann
- läuft komplett lokal, das Passwort wird nirgends gespeichert

## Starten
```
python passwort_pruefer.py
```

## Passwort-Generator
`passwort_generator.py` erzeugt zufällige, sichere Passwörter:
- Länge und Anzahl frei wählbar
- Groß-/Kleinbuchstaben, Ziffern und Sonderzeichen einzeln an- und abschaltbar
- optional ohne verwechselbare Zeichen (l, I, 1, O, 0)
- mindestens ein Zeichen aus jeder gewählten Gruppe
- nutzt das Modul `secrets` (kryptografisch sicherer Zufall statt `random`)

```
python passwort_generator.py
```

## Was ich dabei gelernt habe
<!-- Hier in eigenen Worten 3–4 Punkte ergänzen, zum Beispiel: -->
- Wie man Code in Funktionen aufteilt
- Was Entropie bei Passwörtern bedeutet
- Warum man Passwörter nie im Klartext anzeigt oder speichert
- 

## Ideen für später
- Prüfen, ob das Passwort in bekannten Datenlecks vorkommt
- Eine kleine Weboberfläche dafür bauen
