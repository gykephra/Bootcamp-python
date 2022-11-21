class Game:
    def mvmtUtilisateur(self):
        while True:
            choi = input("\npierre ou (1)/papier ou (2)/ciseaux ou (3), quel est votre choi: ")
            if choi == "1":
                choi = "pierre"
            elif choi == "2":
                choi = "papier"
            elif choi == "3":
                choi = "ciseaux"
            if choi == "pierre" or choi == "papier" or choi == "ciseaux":
                return choi.lower()

    def mvmtOrdinateur(self):
        import random
        tab = ["pierre", "papier", "ciseaux"]
        return random.choice(tab)

    def jeuResultat(self, choiUtilisateur, choiOrdi):
        if choiUtilisateur == choiOrdi:
            return "nul"
        elif choiUtilisateur == "pierre" and choiOrdi == "ciseaux":
            return "gagné"
        elif choiUtilisateur == "ciseaux" and choiOrdi == "papier":
            return "gagné"
        elif choiUtilisateur == "papier" and choiOrdi == "pierre":
            return "gagné"
        else:
            return "perdu"

    def play(self):
        utilisateur = self.mvmtUtilisateur()
        mvmtOrdinateur = self.mvmtOrdinateur()
        resultat = self.jeuResultat(utilisateur, ordinateur)
        print(f"Vous avez choisi {utilisateur} et l'ordinateur {ordinateur}.\nResutats : {resultat}")
        return resultat