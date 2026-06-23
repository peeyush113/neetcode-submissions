# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        resp = 0
        stack = [(root, 0)]

        while stack and k>0:
            node, visited = stack.pop()
            if not node:
                continue

            if visited:
                k -= 1
                resp = node.val
            else:
                stack.append((node.right, 0))
                stack.append((node, 1))
                stack.append((node.left, 0))
        return resp