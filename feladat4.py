print("Ez a program a megadott szöveget a kívánt alkalommal írja ki.")

szoveg = input("Kérem, adja meg a szöveget: ")
darab = int(input("Hányszor szeretné kiíratni? "))

szamlalo = 0

while szamlalo < darab:
    print(szoveg)
    szamlalo += 1
