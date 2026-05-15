# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        resp = []
        if not root:
            return resp
        
        queue = [root]
        qp = 0

        while qp<len(queue):
            res = 0
            qpl = len(queue)
            while qp<qpl:
                node = queue[qp]
                res = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                qp += 1
            resp.append(res)
        return resp