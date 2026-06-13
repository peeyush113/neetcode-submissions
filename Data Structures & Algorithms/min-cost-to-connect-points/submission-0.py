class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [0]*n
        self.count = n
    def find(self, x):
        if x!= self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    def union(self, x, y):
        px, py  = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] > self.rank[py]:
            px, py = py, px

        self.par[py] = px
        self.rank[px] += self.rank[py]
        self.count -= 1
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = []

        for i in range(len(points)):
            xi, yi = points[i]
            for j in range(i, len(points)):
                xj, yj = points[j]
                d = abs(xi-xj) + abs(yi-yj)
                heapq.heappush(heap, [d, i, j])
        
        uf = UnionFind(len(points))
        cost = 0
        while heap:
            w, u, v = heapq.heappop(heap)
            if uf.union(u, v):
                cost += w
        return cost