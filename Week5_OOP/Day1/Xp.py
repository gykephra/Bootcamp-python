#Exercise1

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

#Instancier 03 cats 
cat1 =Cat("Kitti",5)
cat2 =Cat("Catty",4)
cat3 =Cat("cutty",3)


def ancien_chat(cat1,cat2,cat3):
	if(cat1.age>cat2.age and cat1.age>cat3.age):
		print(f"le chat plus agé est==> {cat1.name} , et il a {cat1.age}  ans. ")
	elif(cat2.age>cat1.age and cat2.age>cat3.age):
		print(f"le chat plus agé est==>  {cat2.name} ,et il a {cat2.age}  ans. ")
	elif(cat3.age>cat2.age and cat3.age>cat1.age):
		print(f"le chat plus agé est==>  {cat3.name} , et il a {cat3.age}  ans. ")
	else:
		print("tous égaux")

ancien_chat(cat1,cat2,cha3)


#Exercise2
class Dog:
	def __init__(self,name1,height):
		self.name1 = name1
		self.height = height

	def bark(self) :
		print(f"{self.name1} aboie!")
#
	def jump(self) :
		print(f"{self.name1} saute {self.height*2} cm")
#David's dog
davids_dog=Dog('Medor',55)
print(f'le chien de David s appelle {davids_dog.name1} et son poids est {davids_dog.height}')
davids_dog.bark()
davids_dog.jump()

#lSarah's dog
sarahs_dog=Dog('BO',20)
print(f'le chien de Sarah s appelle {sarahs_dog.name1} et son poids est {sarahs_dog.height}')
sarahs_dog.bark()
sarahs_dog.jump()

#Instruction de comparaison des chiens
if sarahs_dog.height > davids_dog.height:
	print(f"{sarahs_dog.name1} est le plus grand ")
else:
	print(f"{davids_dog.name1} est le plus grand ")



#Exercise3
class Song:
	def __init__(self,lyrics):
		self.lyrics=lyrics

	def sing_me_a_song(self):
		for i in self.lyrics:
			print(i)	

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()



#Exercise4
class Zoo:
	def __init__(self,zoo_name):
		self.animals=[]
		self.zoo_name=zoo_name

	def add_animal(self,new_animal):
		if new_animal not in self.animals:
			self.animals.append(new_animal)
		else:
			print(f"{new_animal} est dejà dans la liste")

	def get_animals(self):
		print('Le zoo est composé de : ')
		for i in self.animals:
			print(i,end=' ')

def sell_animal(self,animal_sold):
		if animal_sold in self.animals:
			self.animals.remove(animal_sold)
		print('Le zoo est composé de : ')
			for i in self.animals:
				print(i,end=' ')


def sort_animals(self):
		tri=sorted(self.animals)
		dict1={}
		result=[]
		x=[]
		for i in tri:
			if i[0] not in x:
				x.append(i[0])
		for i in x:
			p=[]
			for j in tri:
				if j[0]==i:
					p.append(j)
			result.append(p)
		for k,v in enumerate(result):
			dict1[k]=v
		return dict1

	def get_groups(self,dictionnaire):
		print(' ')
		print('Les animaux du Zoo par groupe alphabétique  : ')
		print(dictionnaire)


