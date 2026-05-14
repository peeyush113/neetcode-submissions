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
            return 0
        
        
        if self.rank[X] > self.rank[Y]:
            self.par[Y]  = X
            self.rank[X] += self.rank[Y]
        else:
            self.par[X] = Y
            self.rank[Y] += self.rank[X]
        return 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        connected = n
        for x, y in edges:
            connected -= uf.union(x, y)
            print(connected)
        return connected


        