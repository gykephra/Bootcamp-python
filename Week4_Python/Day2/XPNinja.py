#Exercise1
import math

C = 50
H = 30
D = input("Saisissez quelques nombres séparés par des virgules")
list2 = D.split(",")
print(list2)
for i in list2:
    Q=math.sqrt(((2 * C * int(i))/H))
    print(Q)


#Exercise2
list1= [3, 47, 99, -80, 22, 97, 54, -23, 5, 7] 

print(*list1)

list1.sort(reverse = True) 

print(sum(list1))


sup50=[]
for i in list1:
    if i>50:
        sup50.append(i)

print(sup50)  


for i in list1:
    if i<10:
        inf10.append(i)

print(inf10)   


caree=[]
for i in list1:
    caree.append(i*i)

print(caree) 


newList=list(set(list1))
print(newList)

numbrNum=len(list(set(list1)))
print(numbrNum)



#Exercise3
paragraph="ex ea commodo consequat. Duis aute irure dolor in eu fugiat nulla pariatur. Excepteur sint occaecat " 
print("le paragraphe compte ",len(paragraph.split(" "))," mots")

print("le paragraphe compte ",len(paragraph.split("."))," phase")

print("le paragraphe compte ",len(set(paragraph.split(" ")))," mots unique")


#Exercise4
words = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
words = words.split(" ")
wordsNbr = []
for word in words:
    if word not in wordsNbr:
        wordsNbr.append(word)
for word in wordsNbr:
    numb = 0
    for word1 in words:
        if word == word1:
            numb += 1
    print(f"{word}:{numb}")