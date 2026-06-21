# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # resp = []
        # if not root:
        #     return resp

        # resp.append(root.val)
        # resp.extend(self.preorderTraversal(root.left))
        # resp.extend(self.preorderTraversal(root.right))
        
        # return resp
        resp = []
        if not root:
            return resp
        stack = [root]
        while stack:            
            curr = stack.pop()
            resp.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return resp

        
        # stack = []
        # curr = root
        # resp = []
        # while curr or stack:
        #     if curr:
        #         resp.append(curr.val)                
        #         stack.append(curr.right)
        #         curr = curr.left
        #     else:
        #         curr = stack.pop()
        # return resp