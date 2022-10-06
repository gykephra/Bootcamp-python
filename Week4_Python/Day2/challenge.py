#exo1
numb = input("Tapez un nombre : ")
taille = input("Entrez une longueur : ")
numb1 = []
for i in range(1,int(taille)+1) :
    numb1.append(int(numb)*i)
print(numb1)

#exo2
chaine = input("Input some word: ")
newchaine = ""
for i in chaine :
    if i not in newchaine :
        newchaine += i
print(newchaine)