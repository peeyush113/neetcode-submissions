class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        
        state = [0]*numCourses
        order = []

        def topoSort(node):
            if state[node] == 1:
                return True
            
            if state[node] == 2:
                return False
            
            state[node] = 1
            for ne in graph[node]:
                if topoSort(ne):
                    return True
            state[node] = 2
            order.append(node)
            return False
        
        for course in range(numCourses):
            if topoSort(course):
                return []
        return order
