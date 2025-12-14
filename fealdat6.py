import random

print("Ez a program 20 darab véletlenszámot generál 1 és 12 között.")
print("Csak a 3-mal osztható számokat írja ki.\n")

szamlalo = 0
harommal_oszthato = 0

while szamlalo < 20:
    szam = random.randint(1, 12)
    szamlalo += 1

    if szam % 3 == 0:
        print(f"3-mal osztható szám: {szam}")
        harommal_oszthato += 1

print("\nA program véget ért.")
print(f"Összesen {harommal_oszthato} darab 3-mal osztható szám volt.")
