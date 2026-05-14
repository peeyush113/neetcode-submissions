class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        
        for i, j in prerequisites:
            graph.setdefault(i, []).append(j)
            graph.setdefault(j, [])

        def dfs(course, required):
            if course in required:
                print(course, required)
                return False
            
            required.add(course)
            for c in graph.get(course, []):
                if not dfs(c, required):
                    return False
            required.remove(course)
            return True

        for k in graph.keys():
            if not dfs(k, set()):
                return False
        return True

