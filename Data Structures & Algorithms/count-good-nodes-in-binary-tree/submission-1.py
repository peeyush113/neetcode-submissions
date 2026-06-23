# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        resp = 0
        stack = [(root, -float("inf"))]

        while stack:
            node, max_val = stack.pop()
            if not node:
                continue
            print(node.val, max_val)
            if node.val >= max_val:
                resp +=1 
            max_val = max(node.val, max_val)
            stack.append((node.right, max_val))
            stack.append((node.left, max_val))
        return resp