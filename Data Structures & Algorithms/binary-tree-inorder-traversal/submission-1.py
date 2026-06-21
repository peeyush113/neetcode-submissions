# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        resp = []
        if not root:
            return resp
        
        resp.extend(self.inorderTraversal(root.left))
        resp.append(root.val)
        resp.extend(self.inorderTraversal(root.right))
        return resp