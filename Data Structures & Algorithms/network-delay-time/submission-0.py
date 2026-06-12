class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1, n+1)}
        print(graph)
        for u, v, t in times:
            graph[u].append([t, v])

        heap = [[0, k]]
        res = {}
        while heap:
            t, v = heapq.heappop(heap)
            if v in res:
                continue
            res[v] = t
            for tv, vv in graph[v]:
                if vv not in res:
                    heapq.heappush(heap, [t+tv, vv])
        print(res)
        return max(list(res.values())) if len(res) == n else -1