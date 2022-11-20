#1
numb = input("Saisissez un nombre : ")
length = input("Saisissez une longueur : ")
numb1 = []
for i in range(1,int(length)+1) :
    numb1.append(int(numb)*i)
print(numb1)

#2
word = input("Saisissez une chaine de caractère: ")
word1 = ""
for i in word :
    if i not in word1 :
        word1 += i
print(word1)