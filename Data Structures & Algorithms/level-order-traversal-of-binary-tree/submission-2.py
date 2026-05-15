# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        resp = []
        if not root:
            return resp

        queue = [root]
        queue_index = 0

        while queue_index<len(queue):
            res = []
            for i in range(len(queue)-queue_index):
                node = queue[queue_index]
                queue_index += 1
                
                res.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            resp.append(res)
            # print(resp, res, queue, queue_index)

        return resp

