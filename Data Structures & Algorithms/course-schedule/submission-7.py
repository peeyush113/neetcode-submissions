class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        for src, dst in prerequisites:
            adj[src].append(dst)

        topSort = []
        visit = [0]*numCourses

        def is_cycle(x):
            if visit[x]==1:
                return True
            if visit[x] == 2:
                return False

            visit[x] = 1
            for n in adj[x]:
                if is_cycle(n):
                    return True
            visit[x] = 2
            return False
        
        for i in range(numCourses):
            if is_cycle(i):
                return False
        return True