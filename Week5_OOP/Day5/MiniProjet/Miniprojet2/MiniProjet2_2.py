from MiniProjet2_1 import AnagramChecker as Ana
while True:
    Chx = input("Tapez s pour saisir et q pour quitter")
    print("")
    if Chx.lower() == "s":
        test = Ana()
        mot = test.is_valid_word(input("Entrez votre mot: "))
        if mot:
            print(mot)
            print(test.get_anagrams(mot))
            if test.is_anagram(mot, "RIEN"):
                print(f"nier est un anagramme de {mot}")
            else:
                print(f"nier n'est pas un anagramme de {mot}")
    elif Chx.lower() == "q":
        break
    else:
        print("Entrez s ou q")
