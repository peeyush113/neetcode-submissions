class Solution:

    def dfs(self, k, adj, visited):
        for n in adj[k]:
            if n in visited:
                return False
            
            visited.add(n)
            if not self.dfs(n, adj, visited):
                return False
            visited.remove(n)
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for a, b in prerequisites:
            if a not in adj:
                adj[a] = []
            if b not in adj:
                adj[b] = []
            
            adj[a].append(b)
        
        print(adj)
        for k, v in adj.items():
            visited = set()
            visited.add(k)
            if not self.dfs(k, adj, visited):
                print(k, visited)
                return False
        return True


