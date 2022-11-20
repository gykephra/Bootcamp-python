from datetime import datetime
DateNaiss = input("Donnez votre date de naissance sous le format DD/MM/YYYY : ")
DateNaiss = DateNaiss.split("/")
DateNaiss = int(DateNaiss[-1])
age = str(datetime.now().year - DateNaiss)
age = int(age[-1])
gateau = "       _"

for i in range(int((9-age)/2)) :
    gateau += "_"
for i in range(10-(int((9-age)/2))) :
    if age != 0 :#nombre de bougie
        gateau += "i"
        age -= 1
    else :
        gateau += "_"
gateau += """
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
"""
if (DateNaiss % 4 == 0 and DateNaiss % 100 != 0) or (date % 4 == 0 and date % 100 == 0 and date % 400 == 0) :
    print(gateau)
print(gateau)