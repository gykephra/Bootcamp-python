mot = input("Tapez un mot: ")
mot = {lettre : [mot.index(lettre) for i in lettre] for lettre in mot}
print(mot)
