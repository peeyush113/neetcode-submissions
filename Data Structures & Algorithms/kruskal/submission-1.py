class UnionFind:
    def __init__(self, n) -> None:
        self.parents = list(range(n))
        self.rank = [0] * n
        self.count = n
    
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        px, py= self.find(x), self.find(y)
        if px == py:
            return False
        
        if self.rank[px]> self.rank[py]:
            px, py  = py, px
        self.parents[py] = px
        self.rank[px] += self.rank[py]
        self.count -= 1
        return True

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        heap = []
        for u, v, w in edges:
            heapq.heappush(heap, [w, u, v])
        
        uf = UnionFind(n)
        mst = []
        while len(mst) < n-1 and heap:
            w, u, v = heapq.heappop(heap)
            if uf.union(u, v):
                mst.append(w)
        return sum(mst) if len(mst) >= n-1 else -1