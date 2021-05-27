import random


nacje=['America', 'Arabia', 'Assyria', 'Austria', 'Azte', 'Babylonia', 'Brazilia', 'Byzantin', 'Carthaginia', 'Celti', 'Chines', 'Danis', 'Dutc', 'Egyptia', 'Englis', 'Ethiopia', 'Frenc', 'Germa', 'Gree', 'Hunni', 'Inca', 'India', 'Indonesia', 'Iroquoi', 'Japanes', 'Korea', 'Maya', 'Mongolia', 'Morocca', 'Ottoma', 'Persia', 'Polis', 'Polynesia', 'Portugues', 'Roma', 'Russia', 'Shoshon', 'Siames', 'Songha', 'Spanis', 'Swedis', 'Zulu']
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
    nacja_liczb=(random.randrange(len(nacje)))
    print(a[c]," : ",nacje[nacja_liczb])
    a = a[:c] + a[c + 1:]
    nacje=nacje[:nacja_liczb]+nacje[nacja_liczb+1:]
    if licznik == teams:
        print("-----------------------------------------")
        licznik = 0


    licznik+=1

a=input("Kliknij Enter żeby zakończyć program")
