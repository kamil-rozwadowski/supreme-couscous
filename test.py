import random

a=[]
licznik=1
while 0<1:
    x=input("Podaj imie uczestnika lub napisz 'stop': \n")
    if x.lower()=="stop":
        break
    else:
        a.append(x)

teams= int(input("Podaj rozmiar dużyny: \n"))

for i in a:

    c = random.randrange(len(a))
    print(a[c])
    a = a[:c] + a[c + 1:]

    if licznik == teams:
        print("-----------------------------------------")
        licznik = 0


    licznik+=1

a=input("Kliknij Enter zaby zakończyć program")