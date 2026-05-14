"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, head: Optional['Node']) -> Optional['Node']:
        
        clonedNodes = {}
        def dfs(node):
            if node in clonedNodes:
                return clonedNodes[node]

            clone = Node(node.val)
            clonedNodes[node] = clone
            for n in node.neighbors:
                clone.neighbors.append(dfs(n))            
            return clone
        return dfs(head) if node else None

