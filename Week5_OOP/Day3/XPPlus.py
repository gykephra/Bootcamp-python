#Exercise1
from func import addition as a
print(a(5,5))

#Exercise2
def nbrAleat (nbr) :
    import random as rand
    if nbr in range(0,101):
        if nbr == r.randint(0,100):
            print("Super")
nbrAleat(10)

#Exercise3
import random as rand
import string

mot = "".join([rand.choice(string.ascii_letters) for i in range(0,5)])

print(mot)

#Exercise4
def curr():
    from datetime import datetime, time
    print(datetime.now())

#Exercise5
def Tpsrestant():
    import datetime
    délai = "01/01/2023"
    délai = datetime.datetime.strptime(délai, "%d/%m/%Y")
    periodRst = délai-datetime.datetime.now()
    periodRst1= str(periodRst)
    print(f"il reste {periodRst.days} et {periodRst1[len(periodRst1)-14:len(periodRst1)-7]} heures")

timeperiodRst()

#Exercise6
def duree():
    import datetime
    anniv = input("saisissez votre date d'anniversaire suivant le format DD/MM/YYYY : ")
    anniv = datetime.datetime.strptime(anniv, "%d/%m/%Y")
    minute = datetime.datetime.now() - anniv
    print(f"Vous avez {int(minute.total_seconds()/60)} minutes depuis votre naissance")

duree()

#Exercise7
def dateJour():
    import datetime
    print(datetime.datetime.now())
    vac = "31/07/2023"
    vac = datetime.datetime.strptime(vac, "%d/%m/%Y")
    periodRst = vac-datetime.datetime.now()
    periodRst1 = str(periodRst)
    print(f"il reste {periodRst.days} et {periodRst1[len(periodRst1)-14:len(periodRst1)-7]} heures pour la noël")

dateJour()

#Exercise8
def AgePlanet():
    AgeEnSec = 1000000000
    print(f"Votre age sur Terre est de : {AgeEnSec/31557600} ans.")
    print(f"Votre age sur Mercure est de : {AgeEnSec/(31557600 * 0.2408467)} ans.")
    print(f"Votre age sur Venus est de : {AgeEnSec/(31557600 * 0.61519726)} ans.")
    print(f"Votre age sur Mars est de : {AgeEnSec/(31557600 * 1.8808158)} ans.")
    print(f"Votre age sur Jupiter est de : {AgeEnSec/(31557600 * 11.862615)} ans.")
    print(f"Votre age sur Saturne est de : {AgeEnSec/(31557600 * 29.447498)} ans.")
    print(f"Votre age sur Uranus est de : {AgeEnSec/(31557600 * 84.016846)} ans.")
    print(f"Votre age sur Neptune est de : {AgeEnSec/(31557600 * 164.79132)} ans.")

AgePlanet()
#Exercicse9
users = []
def modFaker(users):
    from faker import Faker
    faker = Faker()
    langue = ['fr','en','aa','af']
    lang = str(faker.sentence(ext_word_list = langue)).split(" ")
    users.append({'nom': faker.name(),'adresse': faker.address(), 'code_langue': lang[0]})

modFaker(users)
modFaker(users)
modFaker(users)
modFaker(users)
print(users)