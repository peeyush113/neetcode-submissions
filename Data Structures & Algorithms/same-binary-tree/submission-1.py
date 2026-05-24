# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def valid_node(self, a, b):
        if a == None and b == None:
            return True

        if a == None or b == None:
            return False
        if a.val == b.val:
            return True
        return False

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True

        if p == None or q == None:
            return False
        
        if p.val != q.val:
            return False

        v = self.valid_node(p, q)
        if not v:
            return v

        lv = self.isSameTree(p.left, q.left)        
        if not lv:
            return lv
        rv = self.isSameTree(p.right, q.right)
        if not rv:
            return rv
        return True
            