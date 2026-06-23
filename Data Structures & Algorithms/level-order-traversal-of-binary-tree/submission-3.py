# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = deque()
        q.append(root)
        resp = []
        while q:
            level_resp = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    level_resp.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level_resp:
                resp.append(level_resp)
        return resp