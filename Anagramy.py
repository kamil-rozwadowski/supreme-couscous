import random

word = input('podaj slowo')
anagram=""

for c in word:
    zmienna = random.randrange(len(word))
    anagram+=word[zmienna]
    word = word[:zmienna] +word[zmienna +1:]
print(anagram)
