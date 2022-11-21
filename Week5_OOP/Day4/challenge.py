# Partie1
class Text:
    def __init__(self, sequence):
        self.sequence = sequence.split(" ")

    def frequent(self, mot):
        return self.sequence.count(mot)

    def courant(self):
        mot = {}
        grand = ""
        for i in self.sequence :
            if i not in mot and mot != {}:
                mot.update({i : self.frequent(i)})
                if mot[grand] < mot[i]:
                    grand = i
            elif mot == {}:
                mot.update({i: self.frequent(i)})
                grand = i
        return grand

    def unique(self):
        return list(set(self.sequence))

    #Partie2
    def from_file(self, nomFic):
        text = ""
        with open(nomFic, "r") as f :
            for x in f :
                text += x[0:len(x)-1]
        return text

a= Text("Un bon livre coûterait maison parfois autant qu'une bonne maison")
print(f"Ce mot {a.frequent('parfois')} est frequent")
print(f"Le mot le plus courant est {a.courant()}")
print(f"les mots uniques sont {a.unique()}")

b = Text(a.from_file('the_stranger.txt'))
print(f"\nCe mot apparait {b.frequent('the')} fois")
print(f"Le mot le plus courant est {b.courant()}")
print(f"les mots uniques sont {b.unique()}")