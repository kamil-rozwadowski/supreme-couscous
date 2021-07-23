import random

STATE = [ ' ','0','0-']
WORDS = ['one','butterfly','lorem','ipsum']
choice = random.choice(WORDS)
live = 3
chars = []
word = len(choice) * "*"
guesses = 0
good = 0

while good != 1 and live != 0:
    print('you have',live,'lives')
    print(STATE[guesses])
    print("guess the word :",word)
    print('used letters: ', chars)
    let = input('give me a letter! \n')
    if let in choice:
        blank = ''
        for x in range(len(word)):
            if let == choice[x]:
             blank = blank + let
            else:
                blank = blank + word[x]
        word = blank
        if let not in chars:
            chars.append(let)
            chars.sort()
        else:
            print('you used already this letter')
    else:
        if let not in chars:
            chars.append(let)
            chars.sort()
            guesses += 1
            live -= 1
        else:
            print('you used already this letter')
    if '*' not in word:
        good=1
if good == 1:
    print('contgratulation you win !!! \n your word is : ',choice)
elif live== 0:
    print('contgratulation you are dead !!! \n 0-k \n your word is: ', choice)