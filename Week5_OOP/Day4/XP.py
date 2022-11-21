#Exercise1
def get_words_from_file():
    with open('mot.txt') as f:
        word = []
        for line in f:
            word.append(line[0:len(line)-1])
    return word

def get_random_sentence(length=6):
    import random
    sentence = ""
    words = get_words_from_file()
    for x in range (0,length):
        sentence += words[random.randint(0,len(words))] + ' '
    return sentence

word = get_random_sentence().lower()
print(word)


def main():
   print("\nCe progamme est un générateur de phrases aléatoires.\n L'utilisateur devra juste entrez la longueur de la phrase, puis la phrase est générée.")
    length = int(input('Entrez la taille de votre phrase mais entre 2 et 20 ==> '))
    if length >= 2 and length <= 20:
        print(get_random_sentence(length))
main()

#Exercice2
import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

sampleJson = json.loads(sampleJson)
print(sampleJson['company']["employee"]['payable']['salary'])

sampleJson['company']['employee'].update({'birth_date':''})
print(sampleJson)

import json
jsonFile = 'fichier.json'
with open(jsonFile,'w') as jF:
    json.dump(sampleJson,jF)