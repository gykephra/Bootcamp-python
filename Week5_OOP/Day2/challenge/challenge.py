class Pagination:
    def __init__(self, items = [], pageSize = 10):
        self.items = items
        self.pageSize = int(pageSize)
        self.current = 0

    def getVisibleItems(self):
        if self.current+self.pageSize != len(self.items)-1 :
            return self.items[self.current:self.current+self.pageSize]
        else:
            return self.items[self.current:len(self.items)]

    def prevPage(self):
        self.current -= self.pageSize

    def nextPage(self):
        self.current += self.pageSize

    def firstPage(self):
        self.current = 0

    def lastPage(self):
        if len(self.items)%self.pageSize == 0 :
            self.current = len(self.items)-self.pageSize
        else :
            self.current = len(self.items)-len(self.items)%self.pageSize

    def goToPage(self,pageNum):
        self.current = pageNum

alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)
print(p.getVisibleItems())
p.nextPage()
print(p.getVisibleItems())
p.nextPage()
print(p.getVisibleItems())
p.prevPage()
print(p.getVisibleItems())
p.lastPage()
print(p.getVisibleItems())
p.firstPage()
print(p.getVisibleItems())
