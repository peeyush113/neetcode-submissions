class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node, parent):
            h = 0
            for ne in adj[node]:
                if ne != parent:
                    h = max(h, 1+dfs(ne, node))
            return h
        
        mh = n
        res = []
        for i in range(n):
            ch = dfs(i, -1)
            if ch == mh:
                res.append(i)
            elif ch<mh:
                res = [i]
                mh = ch
            
        return res