# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        resp = True

        def dfs(node):
            nonlocal resp
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            print(node.val, left, right)
            if abs(left-right) > 1:
                resp = False
            
            return 1+ max(left, right)
        dfs(root)
        return resp