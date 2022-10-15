#Exercise1
from Exercice_XP import Dog
from random import randint

class PetDog(Dog):
	def __init__(self,name,age,weight):
		super().__init__(name,age,weight)
		self.trained=False

	def train(self):
		self.trained=True
		print(self.bark())

	def play(self,*args):
		print(f'{args} all play together')

	def do_a_trick(self):
		if self.trained==True:
			Dressage=[self.name+' does a barrel roll', self.name+' stands on his back legs', self.name+' shakes your hand', self.name+' plays dead']
			val=randint(0,3)
			print(Dressage[val])
		else:
			print(f'{self.name} is not trained ')

BO=PetDog('BO',7,10)
Barky=PetDog('ron',18,20)
Puppy=PetDog('Puppy',10,21)

BO.train()
Barky.train()
BO.fight(Puppy)
BO.play(BO.name,Barky.name,Puppy.name)
BO.do_a_trick()
Puppy.do_a_trick()
Barky.do_a_trick()