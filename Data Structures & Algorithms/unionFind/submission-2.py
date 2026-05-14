class UnionFind:
    
    def __init__(self, n: int):
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, x: int) -> int:
        p = self.par[x]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p        

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        X, Y = self.find(x), self.find(y)
        if X ==Y:
            return False
        
        if self.rank[X] > self.rank[Y]:
            self.par[Y] = X
        elif self.rank[X] < self.rank[Y]:
            self.par[X] = Y
        else:
            self.par[X] = Y 
            self.rank[Y] += 1
        
        return True

    def getNumComponents(self) -> int:

        parents = set()
        for k, v in self.par.items():
            parents.add(self.find(v))
        print(parents, self.par)
        return len(parents)



