import random
#cos
slowo=input("Podaj słowo: \n")
dlugosc=len(slowo)
dlugosc_minus=dlugosc*-1
for i in range(0,dlugosc):
    pozycja = random.randint(dlugosc_minus,dlugosc-1)
    print(slowo[pozycja])