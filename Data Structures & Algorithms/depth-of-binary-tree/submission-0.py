# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def depth(node, d):
            if not node:
                return d

            left = depth(node.left, d+1)
            right = depth(node.right, d+1)
            d = max(left, right)

            return d
        
        return depth(root, 0)