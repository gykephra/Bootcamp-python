from MiniProjet1_1 import Game
# jeu = Game()
# jeu.play()

#Partie2
def get_user_menu_choice():
    choix = input("Pour Jouer encore tapez 1\nPour les scores tapez 2\nQuitter?? tapez 'x' ou 'q': ")
    return choix

def print_results(results):
    print("\tHISTORIQUE\n")
    for x in results:
        print(f"{x} --- Nombre : {results[x]}")

def main():
    results = {
        "gagné": 0,
        "nul": 0,
        "perdu": 0
    }
    while True:
        a = get_user_menu_choice()
        if a == "x" or a == "q":
            print_results(results)
            return 0
        elif a == "1":
            jeu = Game()
            result = jeu.play()
            results.update({result: results[result] + 1})
        elif a == "2":
            print_results(results)
        print("")
main()