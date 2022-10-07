import random

answer=random.randrange(0,100)
nbr=int(input("Donner un chiffre entre 0 et 100 : "))
score=1

while nbr != answer:
    if nbr>100 or nbr<0:
        nbr=int(input("Veuillez donner un chiffre valide entre 0 et 100 : "))
    elif nbr > answer:
        print("Le nombre est plus petit !")
        nbr=int(input("Redonner un chiffre entre 0 et 100 : "))
        score+=1
    elif nbr < answer:
        print("Le nombre est plus grand !")
        nbr=int(input("Redonner un chiffre entre 0 et 100 : "))
        score+=1



print("Bravo vous avez trouvé le chiffre mystère en " + str(score) + " coups, c'était bien le "+ str(answer) + " !" )
    
