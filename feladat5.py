print("Ez a program páros számot kér be a felhasználótól.")

szam = int(input("Kérem, adjon meg egy páros számot: "))

while szam % 2 != 0:
    print("Ez nem páros szám!")
    szam = int(input("Kérem, adjon meg egy páros számot: "))

print("Páros számot adott meg.")
