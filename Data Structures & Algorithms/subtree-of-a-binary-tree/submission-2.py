# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, root, subRoot):
        queue = deque()
        queue.append([root, subRoot])
        while queue:
            a, b = queue.popleft()
            if not a and not b:
                continue
            
            if not a or not b or a.val != b.val:
                return False
            
            queue.append([a.left, b.left])
            queue.append([a.right, b.right])
        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False

        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue

            if node.val == subRoot.val:
                if self.isSameTree(node, subRoot):
                    return True
            stack.append(node.right)
            stack.append(node.left)
        return False



