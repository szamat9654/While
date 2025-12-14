print("Ez a program kiírja a páratlan számokat csökkenő sorrendben 1 és 10 között.")

szam = 10

while szam >= 1:
    if szam % 2 == 1:
        print(szam)
    szam -= 1
