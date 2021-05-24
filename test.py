print('testujemy gita')
print("pomyśl liczbe z zakresu 1 - 100")
def referencja(p,k):
    i = 0
    s=int((p+k)/2)
    print("czy twoja liczba to ",s," : ")
    i=input()
    if i =="tak":
        print("yeeey")
    else:
        print("czy twoja liczba jest większa od ",s,"?")
        a=input()
        if a == "tak":
            referencja(s+1,k)
        else:
            referencja(p,s - 1 )

referencja(1,100)
