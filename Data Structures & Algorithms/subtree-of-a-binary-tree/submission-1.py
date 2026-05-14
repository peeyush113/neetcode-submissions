# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:   
    def identical(self, root, subRoot):
        if not root or not subRoot:
            return not root and not subRoot
        
        if (root.val!=subRoot.val):
            return False

        l = self.identical(root.left, subRoot.left)
        r = self.identical(root.right, subRoot.right)
        return l and r

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return False
            
            if self.identical(node, subRoot):
                return True
            
            return dfs(node.left) or dfs(node.right)

        return dfs(root)
