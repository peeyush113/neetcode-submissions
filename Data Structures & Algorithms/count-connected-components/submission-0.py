class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0
    
    def find(self, n):
        p = self.par[n]
        while  p  != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
    
    def union(self, x, y):
        X, Y = self.find(x), self.find(y)
        if X == Y:
            return False
        
        if self.rank[X] < self.rank[Y]:
            self.par[X]  = Y
        elif self.rank[X] > self.rank[Y]:
            self.par[Y] = X
        else:
            self.par[Y] = X
            self.rank[X] += 1
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for x, y in edges:
            uf.union(x, y)
        
        connected = set()
        for i in range(n):
            p = uf.find(i)
            connected.add(p)

        return len(connected)


        