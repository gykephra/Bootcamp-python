#Exercise3

>>> 3 <= 3 < 9 	 # true
>>> 3 == 3 == 3  # true
>>> bool(0)      # false
>>> bool(5 == "5")#false
>>> bool(4 == 4) == bool("4" == "4") # true
>>> bool(bool(None))  # false

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x) # x is True
print("y is", y)  # y is False
print("a:", a) # a: 5
print("b:", b)  # b: 10



#Exercise4
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit,sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.Duis aute irure dolor in reprehenderit in voluptate velitesse cillum dolore eu fugiat nulla pariatur.Excepteur sint occaecat cupidatat non proident,sunt in culpa qui officia deserunt mollit anim id est laborum."
print(len(my_text)) 

#Exercise5
while 1 :
    phrase = input("Entrez la phrase la plus longue possible sans le caractère A ")
    test = 0
        for x in phrase :
            if x == "A" :
                test = 1
        if test == 1 :
            print("Il ya un 'A'")
        else :
            print("Félicitations")
    else :
        break