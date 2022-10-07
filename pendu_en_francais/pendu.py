from dataclasses import replace
import random
import unicodedata

word=(random.choice(open('fr.txt').read().split()).strip())
print(word)
word = unicodedata.normalize('NFD', word).encode('ascii', 'ignore').decode("utf-8")

print(word)
wordLen=len(word)
wordList=list(word)
wordFind=[]
score=0
maxAttempt=wordLen*3



def displayWord():
    wordGraph=""
    for i in range(wordLen):
        wordGraph=wordGraph+wordFind[i]+" "

    print(wordGraph)





for i in range(wordLen):
    wordFind.append("-")

displayWord()

while wordFind != wordList and maxAttempt > 0:

    letter=input("Donnez une lettre : ")
    letter=letter.lower()
    score+=1
    maxAttempt=maxAttempt-1
    print("Nomre d'essais restant : " + str(maxAttempt))
    for i in range(wordLen):
        if letter == wordList[i]:
            wordFind[i]=letter

    displayWord()

print()
if maxAttempt != 0:
    print("Gagné  en " + str(score) + " coups !")
else:
    print("Dommage vous avez perdu ... le mot était " + word)
print()