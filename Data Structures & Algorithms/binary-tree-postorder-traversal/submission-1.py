# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        resp = []
        if not root:
            return resp

        # if root.left:
        #     resp.extend(self.postorderTraversal(root.left))
        # if root.right:
        #     resp.extend(self.postorderTraversal(root.right))
        # resp.append(root.val)
        # return resp

        stack = [(root, 0)]
        while stack:
            curr, visited = stack.pop()
            if visited:
                resp.append(curr.val)
            else:
                stack.append((curr, 1))
                if curr.right:
                    stack.append((curr.right, 0))
                if curr.left:
                    stack.append((curr.left, 0))
        return resp

