# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        stack = [(root, [-float("inf"), float("inf")])]
        while stack:
            node, rg  = stack.pop()
            if not node:
                continue
            if node.val <= rg[0] or node.val >= rg[1]:
                return False
            if node.left and node.val <= node.left.val:                
                return False
            if node.right and node.val >= node.right.val:
                return False
            
            stack.append((node.right, [node.val, rg[1]]))
            stack.append((node.left, [rg[0], node.val]))
        return True
            
