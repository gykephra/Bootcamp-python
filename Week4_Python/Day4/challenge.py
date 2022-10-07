matrix = [
	["7","i","3"],
	["T","s","i"],
	["h","%","x"],
	["i","","#"],
	["s","M",""],
	["$","a",""],
	["#","t","%"],
	["^","r","!"]
]

def read(liste,index,*args):
    return liste[index]
code=[]
lect = 0
while lect < (len(Matrix[0])):
    i=0
    for line in Matrix :
        char = read(line,lect)
        if char.isalpha() and char != " ":
            code.append(char)
            i=0
        elif i==0:
            i += 1
        elif i==1:
            code.append(" ")
            i += 1

    lect +=1
print("".join(code))