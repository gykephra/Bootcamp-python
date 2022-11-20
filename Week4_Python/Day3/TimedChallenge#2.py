Mt = input("Entrez une Sentence : ")
Mt = Mt.split(" ")
Sentence = ""
for x in range(len(Mt)-1,-1,-1) :
    Sentence += Mt[x] + " "
    print(x)
print(Sentence)