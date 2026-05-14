class Node:
    def __init__(self, total, i, j):
        self.total = total
        self.left = None
        self.right = None

        self.i = i
        self.j = j
        self.m = (i+j)//2

class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self.head = self.build(nums, 0, len(nums)-1)

    @staticmethod
    def build(nums, l, r):
        root = Node(0, l, r)
        if l == r:
            root.total = nums[l]
        else:        
            m = (l+r)//2
            
            root.left = SegmentTree.build(nums, l, m)
            root.right = SegmentTree.build(nums, m+1, r)

            root.total = root.left.total + root.right.total
        return root

    def update(self, index: int, val: int) -> None:
        
        def updateNode(node, i, v):
            if node.i == node.j:
                node.total = v
            else:
                if i > node.m:
                    updateNode(node.right, i, v)
                else:
                    updateNode(node.left, i, v)
                node.total = node.left.total + node.right.total
            return node.total
        
        updateNode(self.head, index, val)

    def query(self, L: int, R: int) -> int:
        
        def qNode(node, L, R):
            if node.i == L and node.j == R:
                return node.total

            if node.m < L:
                return qNode(node.right, L, R)
            elif node.m >= R:
                return qNode(node.left, L, R)
            else:
                return qNode(node.left, L, node.m) + qNode(node.right, node.m+1, R)
        return qNode(self.head, L, R)
