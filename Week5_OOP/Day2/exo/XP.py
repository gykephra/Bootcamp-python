#Exercise1
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Siamese(Cat):
	def sing(self, sounds):
		return f'{sounds}'


Beng=Bengal('catty',12)
Chart=Chartreux('charia',11)
Sia=Siamese('lynx',10)
all_cats=[Beng,Chart,Sia]

sara_pets=Pets(all_cats)

sara_pets.walk()

#Exercise2
class Dog():
	def __init__(self,name, age, weight):
		self.name=name
		self.age=age
		self.weight=weight

	def bark (self):
		Aboiement=self.name+' aboie'
		return Aboiement

	def run_speed(self):
		vitesse=((self.weight/self.age)*10)
		return vitesse

	def fight(self,dogg):
		weight1=self.run_speed()*self.weight
		weight2=dogg.run_speed()*dogg.weight
		if weight1>weight2:
			print(self.name,f' with weight = {weight1} win against ',dogg.name,f' with weight= {weight2}')
		elif(weight1==weight2):
			print(f'{self.name} and {dogg.name} sont égaux')
		else:
			print(f'{dogg.name} with weight = {weight2} win against {self.name} with weight = {weight1}')

BO=Dog('BO',14,11)
Barky=Dog('Barky',17,12)
Puppy=Dog('Puppy',23,9)

print(BO.bark())
print(BO.name,' vitesse = ',BO.run_speed())
print(Puppy.bark())
print(Puppy.name,' vitesse = ',Puppy.run_speed())
print(Barky.bark())
print(Barky.name,' vitesse = ',Barky.run_speed())
BO.fight(Barky)
BO.fight(Puppy)
BO.fight(BO)
Barky.fight(Puppy)