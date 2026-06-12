class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        res = {i: -1 for i in range(n)}
        heap = [[0, src]]
        heapq.heapify(heap)

        graph = {}
        for i in range(n):
            graph[i] = []

        for u, v, w in edges:
            graph[u].append([v, w])

        while heap:
            w, node = heapq.heappop(heap)
            if res[node] != -1:
                continue

            res[node] = w
            for neb, nw in graph[node]:
                if res[neb] == -1:
                    heapq.heappush(heap, [w + nw, neb])
        return res
