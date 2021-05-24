import random
x = random.randint(1,10)
numerator=0
while True:
    odp=int(input('zgadnij liczbe'))
    numerator +=1
    if odp == x:
         print('Brawo ci sie za', numerator,'razem' )
         break
    elif odp < x:
        print('za mało')
    elif odp > x:
        print('za duzo')
