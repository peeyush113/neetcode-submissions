# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        
        queue = [[root, 0]]
        op = []
        while queue:
            node, level = queue[0]
            queue = queue[1:]
            if len(op) <=level:
                op.append([])
            op[level].append(node.val)
            level +=1 
            if node.left:
                queue.append([node.left, level])
    
            if node.right:
                queue.append([node.right, level])
        

        return op
