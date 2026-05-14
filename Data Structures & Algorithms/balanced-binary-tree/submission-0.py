# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(node):
            if not node:
                return True, 0
            
            balanced, left = height(node.left)
            if not balanced:
                return False, left+1 

            balanced, right = height(node.right)
            if not balanced:
                return False, right+1
            
            if abs(left-right) > 1:
                return False, max(left, right)+1
            return True, max(left, right)+1
        
        balanced, h = height(root)
        return balanced 



