"""
Passwort-Prüfer
Prüft, wie sicher ein Passwort ist, und gibt Verbesserungstipps.
Alles läuft lokal – das Passwort wird nirgends gespeichert oder verschickt.
"""

import getpass
import math
import string

# Eine kleine Liste sehr häufiger Passwörter, die man nie verwenden sollte
HAEUFIGE_PASSWOERTER = {
    "123456", "123456789", "12345678", "passwort", "password", "qwertz",
    "qwerty", "hallo123", "111111", "abc123", "iloveyou", "admin", "welcome",
}


def zeichenvorrat(passwort):
    """Zählt, aus wie vielen möglichen Zeichen das Passwort gebaut ist."""
    vorrat = 0
    if any(z in string.ascii_lowercase for z in passwort):
        vorrat += 26  # Kleinbuchstaben
    if any(z in string.ascii_uppercase for z in passwort):
        vorrat += 26  # Großbuchstaben
    if any(z in string.digits for z in passwort):
        vorrat += 10  # Ziffern
    if any(z in string.punctuation for z in passwort):
        vorrat += 32  # Sonderzeichen
    return vorrat


def staerke_in_bits(passwort):
    """Schätzt die Stärke (Entropie) in Bit: Länge × log2(Zeichenvorrat)."""
    vorrat = zeichenvorrat(passwort)
    if vorrat == 0:
        return 0
    return len(passwort) * math.log2(vorrat)


def pruefe(passwort):
    """Gibt eine Bewertung und eine Liste mit Tipps zurück."""
    tipps = []

    if passwort.lower() in HAEUFIGE_PASSWOERTER:
        return "sehr schwach", ["Dieses Passwort steht auf jeder Liste von Hackern. Bitte nicht verwenden!"]

    if len(passwort) < 12:
        tipps.append("Mindestens 12 Zeichen verwenden.")
    if not any(z.isupper() for z in passwort):
        tipps.append("Großbuchstaben hinzufügen.")
    if not any(z.islower() for z in passwort):
        tipps.append("Kleinbuchstaben hinzufügen.")
    if not any(z.isdigit() for z in passwort):
        tipps.append("Ziffern hinzufügen.")
    if not any(z in string.punctuation for z in passwort):
        tipps.append("Sonderzeichen hinzufügen, z. B. ! ? # %.")

    bits = staerke_in_bits(passwort)
    if bits < 40:
        bewertung = "schwach"
    elif bits < 60:
        bewertung = "mittel"
    elif bits < 80:
        bewertung = "stark"
    else:
        bewertung = "sehr stark"

    return bewertung, tipps


def main():
    print("=== Passwort-Prüfer ===")
    # getpass versteckt die Eingabe, damit niemand mitlesen kann
    passwort = getpass.getpass("Passwort eingeben (wird nicht angezeigt): ")

    bewertung, tipps = pruefe(passwort)
    print(f"\nBewertung: {bewertung}")
    print(f"Geschätzte Stärke: {staerke_in_bits(passwort):.0f} Bit")

    if tipps:
        print("\nSo wird es sicherer:")
        for tipp in tipps:
            print(f"  - {tipp}")
    else:
        print("\nSehr gut, keine Verbesserungen nötig!")


if __name__ == "__main__":
    main()
