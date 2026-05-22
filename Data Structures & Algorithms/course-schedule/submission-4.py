class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for a, b in prerequisites:
            adj[a].append(b)
        
        visited = set()
        top_sort = []
        def dfs(node):
            
            if node in visited:
                return False
            if not adj[node]:
                return True

            visited.add(node)
            for n in adj[node]:
                if not dfs(n):
                    return False
                    
            visited.remove(node)
            adj[node] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
