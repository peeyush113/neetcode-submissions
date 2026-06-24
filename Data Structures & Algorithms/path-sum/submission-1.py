# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def dfs(node):
            nonlocal targetSum
            if not node:
                return False
            
            targetSum -= node.val
            if not node.left and not node.right and targetSum == 0:
                return True
            
            if dfs(node.left) or dfs(node.right):
                return True
            targetSum += node.val
            
            return False
        return dfs(root)