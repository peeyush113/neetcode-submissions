class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = {i:[] for i in range(n)}
        for i, edge in enumerate(edges):
            x, y = edge
            graph[x].append([succProb[i], y])
            graph[y].append([succProb[i], x])

        heap = [[-1, start_node]]
        visited = set()
        while heap:
            p, y = heapq.heappop(heap)
            p = p*-1
            if y == end_node:
                return p
            if y in visited:
                continue
            visited.add(y)
            for py, yy in graph[y]:
                if yy not in visited:
                    heapq.heappush(heap, [p*py*-1, yy])
        return 0