#Exercise1
import json
file  = "C:/Users/FANOSERVICES/Documents/Full_Stack_Coding_Bootcamp_Python_Full_Time/Week_5/Day_4/Exercice XP OR/restaurant_menu.json"

with open(file) as f:
    data = json.load(f)
try:
    print(len(data["valentine_items"]))
except:
    data["valentine_items"] = []
 

name = input(" Valentines Day item name: _\t")
isMeal = input(" If Valentines Day item name is a meal put (yes or no): _\t")
price = input(" Valentines Day item price: _\t")

import re

def regEx():

    total_words = len(re.split("\s",name))
    x = re.findall(r"\A[V]", name)
    y= re.findall(r"\b[A-Z]",name)
    if not(x) and len(y)!=total_words:
        return False

    w = re.findall("e",name)
    if isMeal.lower() != "yes" or len(w)<2:
        return False
    d = re.findall("[0-9]",name)
    if len(d)!=0:
        return False

    z = re.findall("[0-9][0-9],14$",price)
    if not(z):
        return False
    return True

def add_valentine_item(name, price,data):
    dict = {
        "name":name,
        "price":price
    }
    data["valentine_items"].append(dict)
    return data

print(regEx)
if  regEx():
    add_valentine_item(name, price,data)
    print(data)
    with open(file,"w") as f:
        json.dump(data,f,indent = 3,sort_keys = True)
    print("Sweat heart")
else:
    print("Your item don't follow the rules of a valentine's item")
    print("Exemple : :::::::::::::::::::::\nName: Vegetable Soup of Valentines-day\nPrice: 45,14")


#Exercise2
import random
import json
class Character():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.strength = self.rand_points()
        self.dexterity = self.rand_points()
        self.constitution = self.rand_points()
        self.intelligence = self.rand_points()
        self.wisdom =self.rand_points()
        self.charisma = self.rand_points()

    def rand_points(self):
        liste = [random.randint(1,6) for i in range(4)]
        return sum(liste) - min(liste)

class Game():
    def start(self):
        all_players = {} 
        all_players["players"] = []
        players = input("How many players are playing:\t_ ")
        try:
            num = int(players)
        except:
            print("Your entry not correct")
        for i in range(num):
            name = input(f"Chararcter number {i} name:\t_ ")
            age = input(f"Chararcter number {i} age:\t_ ")
            character = Character(name,age)
            file = f"C:\Users\USER\Documents\Bootcamp-python\Week5_OOP\Day4\XPNinja{character.name}.txt"   
            with open(file,"w") as f:
                f.write(f"Name : {character.name}\n")
                f.write(f"Age : {character.age}\n")
                f.write(f"----\tStats  ----\n")
                f.write(f"Strength : {character.strength}\n")
                f.write(f"Dexterity : {character.dexterity}\n")
                f.write(f"Constitution : {character.constitution}\n")
                f.write(f"Intelligence : {character.intelligence}\n")
                f.write(f"Wisdom : {character.wisdom}\n")
                f.write(f"Charisma : {character.charisma}\n")
            dict = {
                "Name" : character.name,
                "Age" :character.age,
                "Strength" : character.strength,
                "Dexterity" : character.dexterity,
                "Constitution": character.constitution,
                "Intelligence" : character.intelligence,
                "Wisdom" : character.wisdom,
                "Charisma" : character.charisma
            }
            all_players["players"].append(dict)
        json_file = "C:\Users\USER\Documents\Bootcamp-python\Week5_OOP\Day4\XPNinja\gamers.json"
        with open(json_file,"w") as f:
            json.dump(all_players,f,indent = 3)
        print("Game initiated with success")

game = Game()
game.start()