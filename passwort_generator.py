"""
Passwort-Generator
Erzeugt zufällige, sichere Passwörter.
Alles läuft lokal – die Passwörter werden nirgends gespeichert oder verschickt.
"""

import math
import secrets
import string

# Zeichen, die man leicht verwechselt (z. B. l, 1, I, O, 0)
VERWECHSELBAR = set("lI1O0o")


def baue_zeichengruppen(gross=True, klein=True, ziffern=True, sonderzeichen=True,
                        ohne_verwechselbare=False):
    """Gibt eine Liste der gewählten Zeichengruppen zurück."""
    gruppen = []
    if klein:
        gruppen.append(string.ascii_lowercase)
    if gross:
        gruppen.append(string.ascii_uppercase)
    if ziffern:
        gruppen.append(string.digits)
    if sonderzeichen:
        gruppen.append(string.punctuation)

    if ohne_verwechselbare:
        gruppen = ["".join(z for z in g if z not in VERWECHSELBAR) for g in gruppen]

    return [g for g in gruppen if g]


def erzeuge_passwort(laenge=16, **optionen):
    """
    Erzeugt ein zufälliges Passwort.
    Aus jeder gewählten Zeichengruppe kommt mindestens ein Zeichen vor.
    """
    gruppen = baue_zeichengruppen(**optionen)
    if not gruppen:
        raise ValueError("Mindestens eine Zeichengruppe muss ausgewählt sein.")
    if laenge < len(gruppen):
        raise ValueError(f"Die Länge muss mindestens {len(gruppen)} sein.")

    alle_zeichen = "".join(gruppen)

    # secrets statt random: secrets ist für Passwörter gedacht (kryptografisch sicher)
    zeichen = [secrets.choice(g) for g in gruppen]
    zeichen += [secrets.choice(alle_zeichen) for _ in range(laenge - len(gruppen))]

    # Mischen, damit die Pflichtzeichen nicht immer am Anfang stehen
    secrets.SystemRandom().shuffle(zeichen)
    return "".join(zeichen)


def staerke_in_bits(laenge, **optionen):
    """Schätzt die Stärke (Entropie) in Bit: Länge × log2(Zeichenvorrat)."""
    vorrat = len("".join(baue_zeichengruppen(**optionen)))
    if vorrat == 0:
        return 0
    return laenge * math.log2(vorrat)


def frage_ja_nein(frage, standard=True):
    """Stellt eine Ja/Nein-Frage. Enter übernimmt den Standardwert."""
    hinweis = "[J/n]" if standard else "[j/N]"
    antwort = input(f"{frage} {hinweis}: ").strip().lower()
    if antwort == "":
        return standard
    return antwort in ("j", "ja", "y", "yes")


def frage_zahl(frage, standard, minimum=1, maximum=128):
    """Fragt nach einer Zahl, bis eine gültige eingegeben wird."""
    while True:
        antwort = input(f"{frage} [{standard}]: ").strip()
        if antwort == "":
            return standard
        if antwort.isdigit() and minimum <= int(antwort) <= maximum:
            return int(antwort)
        print(f"  Bitte eine Zahl zwischen {minimum} und {maximum} eingeben.")


def main():
    print("=== Passwort-Generator ===")

    laenge = frage_zahl("Wie lang soll das Passwort sein?", 16, minimum=4)
    anzahl = frage_zahl("Wie viele Passwörter?", 1, maximum=20)
    optionen = {
        "gross": frage_ja_nein("Großbuchstaben verwenden?"),
        "klein": frage_ja_nein("Kleinbuchstaben verwenden?"),
        "ziffern": frage_ja_nein("Ziffern verwenden?"),
        "sonderzeichen": frage_ja_nein("Sonderzeichen verwenden?"),
        "ohne_verwechselbare": frage_ja_nein("Verwechselbare Zeichen (l, I, 1, O, 0) weglassen?", False),
    }

    try:
        passwoerter = [erzeuge_passwort(laenge, **optionen) for _ in range(anzahl)]
    except ValueError as fehler:
        print(f"\nFehler: {fehler}")
        return

    print("\nDeine Passwörter:")
    for pw in passwoerter:
        print(f"  {pw}")

    bits = staerke_in_bits(laenge, **optionen)
    print(f"\nGeschätzte Stärke: {bits:.0f} Bit")
    if bits < 60:
        print("Tipp: Mehr Länge oder mehr Zeichengruppen machen das Passwort deutlich sicherer.")


if __name__ == "__main__":
    main()
