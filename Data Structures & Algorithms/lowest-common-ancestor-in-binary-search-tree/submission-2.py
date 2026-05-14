# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            l, h = q, p
        else:
            l, h = p, q


        def dfs(node):
            if node.val >= l.val and node.val <= h.val:
                return node

            if node.val < l.val:
                return dfs(node.right)
            else:
                return dfs(node.left) 
        return dfs(root)