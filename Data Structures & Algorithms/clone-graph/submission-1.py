"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        
        def dfs(curr):
            if curr in visited:
                return visited[curr]
            
            n = Node(curr.val)
            visited[curr] = n
            for ne in curr.neighbors:
                n.neighbors.append(dfs(ne))
            return n
        return dfs(node) if node else None

