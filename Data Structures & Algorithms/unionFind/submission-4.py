class UnionFind:
    
    def __init__(self, n: int):
        self.parents = list(range(n))
        self.rank = [0]*n
        self.count = n

    def find(self, x: int) -> int:
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)

        if px == py:
            return False
        
        if self.rank[px] > self.rank[py]:
            px, py = py, px
        
        self.parents[py] = px
        self.rank[px] += self.rank[py]

        self.count -=1 
        return True

    def getNumComponents(self) -> int:
        return self.count

