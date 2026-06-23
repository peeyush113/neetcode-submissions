# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        resp = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                resp.append("#")
                continue
            resp.append(str(node.val))
            stack.append(node.right)
            stack.append(node.left)
        return ",".join(resp)
            
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(",")
        index = 0
        def dfs():
            nonlocal index
            if index >= len(data):
                return None
            val = data[index]
            index += 1
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        root = dfs()
        return root



