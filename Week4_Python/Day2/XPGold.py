#Exercise1
list0 = ['A', 10, 'b']
list1=['B', 15, 'salut']
list10=list0.extend(list1)
print(list10)

#Exercise2
for numb in range(1500,2501):
	if numb%5==0 or numb%7==0:
		print(numb)

#Exercise3
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
name=input("Saisissez votre nom\n")
for nam in names:
	if nam==name:
		print(names.index(nam))
		break



#Exercice4
numb = input("Input the 1st number: ")
numb1 = input("Input the 2nd number: ")
if numb1 > numb :
    numb = numb1
numb1 = input("Input the 3rd number: ")
if numb1 > numb :
    numb = numb1
print("The greatest number is",numb)

#Exercise5
import string
Alphabet=list(string.ascii_lowercase)
voyelle=["a","e","i","o","u","y"]
for alpha in Alphabet:
	if alpha in voyelle:
		print(alpha,"est une voyelle")
	else:
		print(alpha,"est une consomne")
			

#Exercise6
words=[]
lettre=input("Saisissez une lettre")
for i in range(1,8):
	mot=input("Saisissez un mot")
	words.append(mot)

for i in words:
	if lettre in i:
		print(i.index(lettre))
	else:
		print(lettre," n'est pas dans ",i)

#Exercise7
list1=[]
for nb in range(1,1000001):
	list1.append(nb)
print(min(list1))
print(max(list1))
print("la somme est ",sum(list1))


#Exercise8
seq=input("Saisissez des valeurs separees par des virgules")
print(seq.split(","))
print(tuple(seq.split(",")))
