# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        resp = []
        stack = [(root, 0)]

        while stack:
            node, visited = stack.pop()
            if not node:
                continue

            if visited:
                resp.append(node.val)
            else:
                stack.append((node.right, 0))
                stack.append((node, 1))
                stack.append((node.left, 0))
        return resp[k-1]