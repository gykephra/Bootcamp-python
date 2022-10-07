#Exercise1
my_fav_numbers = [7,5,8]
my_fav_numbers = my_fav_numbers + [1,3]
my_fav_numbers.pop(-1)
friend_fav_numbers = [15,18]
our_fav_numbers = my_fav_numbers + friend_fav_numbers
print(our_fav_numbers)

#Exercise2
tpl = (7)
#tpl = tpl + (9)
#TypeError: unsupported operand type(s) for +: 'int' and 'tuple'

#Exercice 3 : Liste
basket = ["Banana", "Apples", "Oranges", "Blueberries"];
basket.remove("Banana")
del basket[3]
basket.append("Kiwi")
basket.append("Apples")
nbApple=0;
for fruit in basket :
    if "Apples" == fruit :
        nbApple += 1
print(nbApple)
basket = []
print(basket)

#Exercise4
#floats= nombres à virgule,  nombres decimaux. entiers = nombres complets, sans virgule
numb = 1
list1 = []
while nbr <5 :
    numb += 0.5
    list1.append(nbr)
print(list1)

#Exercise5
for i in range(1,21):
        print(i)

for i in range(1,21):
     if i%2 == 0 :
        print(i)

#Exercice6
while(1) :
    nom = input("Tapez votre nom ")
    if nom.lower() == "ephraim" :
        break

#Exercise7
fruits = input("Tapez  votre/vos fruits préférés séparés par un espace")
fruit = fruits.split(" ")
print(fruit)

fruit1 = input("Tapez le nom d'un fruit")
if fruit1 in fruits :
    print("Vous avez choisi l'un de vos fruits préférés ! Prendre plaisir!")
else :
    print("Vous avez choisi un nouveau fruit. J'espère que tu apprécies")

#Exercise8
garniture = ""
garnitures = ""
prix = 10;
while garniture.lower() != "quitter" :
    garniture = input("Entrez une serie de garnitures de pizza")
    if garniture.lower() != "quitter" :
        print("Nous ajouterons "+ garniture+" à votre pizza")
        garnitures += garniture + " "
    prix += 2.5

print("Votre pizza est composé de", garnitures," Et le prix total est :",prix)

#Exercise9
age = input("Tapez l'âge de la 1 ère personne")
prix = 0
while age.lower() != "fin" :
    if int(age) < 3 :
        print("C'est gratuit pour toi")
    elif int(age) <= 12 :
        prix += 10
        print("Tu paies 10$")
    else :
        prix += 15
        print("Tu paies 15$")
    age = input("Entrez l'âge d'une autre personne ou 'fin' pour avoir le prix total :")
print(prix)

#Exercise10
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = []

while 1 :
    pret = input("Un sandwich pret? 'oui' ou 'non' ")
    if pret.lower() == "oui" and sandwich_orders != []:
       finished_sandwiches.append(sandwich_orders[0])
       sandwich_orders.remove(sandwich_orders[0])
        if len(sandwich_orders) != 0 :
            print("Plus que", len(sandwich_orders))
        else :
            print("Finish")
    elif sandwich_orders == [] :
        print("Listes des sandwich préparés :")
        for sandwich in finished_sandwiches :
            print(sandwich)
        break
    else :
        print("Je patiente")

#Exercise11
sandwich_orders = ["Pastrami sandwich", "Tuna sandwich", "Avocado sandwich","Pastrami sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = []
while 1 :
    if "Pastrami sandwich" in sandwich_orders :
        sandwich_orders.remove("Pastrami sandwich")
    else :
        break
print("Plus de Pastrami sandwich")
while sandwich_orders != [] :
    pret = input("Un sandwich pret? 'oui' ou 'non' ")
    if fini.lower() == "oui" and sandwich_orders != []:
        finished_sandwiches.append(sandwich_orders[0])
        sandwich_orders.remove(sandwich_orders[0])
        if len(sandwich_orders) != 0 :
            print("Plus que", len(sandwich_orders))
        else :
            print("Finish")
    else :
        print("Je patiente")

print("Listes des sandwich préparés :",finished_sandwiches)
