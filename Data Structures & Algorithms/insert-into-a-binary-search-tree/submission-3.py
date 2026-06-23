# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        valNode = TreeNode(val)
        if not root:
            return valNode

        node = root
        prev = node
        while node:
            prev = node
            if val < node.val:
                node = node.left
            else:
                node = node.right
        
        if val > prev.val:
            prev.right = valNode
        else:
            prev.left = valNode
        return root