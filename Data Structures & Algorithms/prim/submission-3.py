class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for u, v, w in edges:
            adj[u].append([v, w])
            adj[v].append([u, w])
        
        heap = []
        for nei, w in adj[0]:
            heapq.heappush(heap, [w, 0, nei])
        
        mst = 0
        visit = set()
        visit.add(0)
        while len(visit) < n and heap:
            w, u, v = heapq.heappop(heap)
            if v in visit:
                continue
            
            mst += w
            visit.add(v)
            for nei, nw in adj[v]:
                if nei not in visit:
                    heapq.heappush(heap, [nw, v, nei])
        return mst if len(visit) == n else -1