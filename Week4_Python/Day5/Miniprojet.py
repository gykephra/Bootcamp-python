import random

TabMots = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
mot = random.choice(TabMots) 
def playTheGame():								
	print('la liste des mots')
	print(TabMots)
	mot1=input('prenez un mot :')
	while(mot1 not in TabMots):
		mot1=input(' le mot choisi nest pas parmi la liste des mots :')
	hiddenWrd = "*"*len(mot)
	print(hiddenWrd)
	hid = mot.split("");
playTheGame()