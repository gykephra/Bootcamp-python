nbr = int(input("Saisisez un nombre : "))
NbrP = 0
for i in range(1,nbr) :
    if nbr%i == 0 :
        NbrP += i
if NbrP == nbr :
    print(nbr,"est un nbr NbrP")
else :
    print(nbr,"n'est pas un nbr NbrP")