class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(1, n+1):
            self.par[i] = i
            self.rank[i] = 0
        
    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
    
    def union(self, x, y):
        X, Y = self.find(x), self.find(y)
        if X == Y:
            return False
        
        if self.rank[X] > self.rank[Y]:
            self.par[Y] = X
        elif self.rank[X]<self.rank[Y]:
            self.par[X] = Y
        else:
            self.par[X] = Y
            self.rank[Y] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        resp = []
        for x,y in edges:
            if not uf.union(x, y):
                resp.append([x, y])
        return resp[-1]



        