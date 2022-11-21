class Circle:
    def __init__(self, radius):
        self.radius = radius

    def surface(self):
        import math
        return math.pi * self.radius

    def __add__(self, other):
        return self.radius + other.radius

    def comp(self, other):
        if self.radius < other.radius :
            return f"Le cercle ayant {other.radius} comme rayon est le plus grand."
        elif self.radius > other.radius :
            return f"Le cercle ayant {self.radius} comme rayon est le plus grand."
        return "Egalité"

    def egal(self, other):
        if self.radius == other.radius:
            return True
        return False

    def trie(self,*args):
        tab = []
        for i in args:
            tab.append(i)
        for i in range(0,len(tab)):
            tmp = tab[i]
            j=i-1
            while j>=0 and tab[j].radius > tmp.radius:
                tab[j+1] = tab[j]
                j=j-1
            tab[j+1] = tmp
            print(tab)
        return tab

crcl = Circle(10)
asp  = Circle(60)
asp1  = Circle(12)
asp2  = Circle(50)
asp3  = Circle(150)
asp4  = Circle(300)
print(crcl)
print(crcl.surface())
print(crcl.comp(asp))
print(crcl.egal(asp))
tab = crcl.trie(asp,asp1,asp2,asp3,asp4)
for i in tab :
    print(i.radius)