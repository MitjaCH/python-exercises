# 6. Zahlenraten

import random

# Wähle eine zufällige Zahl zwischen 1 und 10.
# Frage den Benutzer, eine Zahl zu raten.
# Benutze eine Schleife, um das Raten zu wiederholen, bis der Benutzer richtig rät.
# Gib Hinweise, ob die Zahl zu hoch oder zu niedrig ist.

# Auf Zeile 3 wird random importiert das ist ein Package aus Python die folgendes ermöglicht:

# Mit random.randint() können wir eine zufällige Zahl im Bereich 1 bis 10 erzeugen.
zufallszahl = random.randint(1, 10)
print(zufallszahl)