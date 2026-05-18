class SegmentNode:

    def __init__(self, total, li, ri) -> None:
        self.total = total
        self.li = li
        self.ri = ri
        self.left: SegmentNode|None = None
        self.right: SegmentNode|None = None

    @staticmethod
    def build(nums, L, R):
        if L == R:
            return SegmentNode(nums[L], L, R)

        m = (L+R)//2
        root = SegmentNode(0, L, R)
        root.left = SegmentNode.build(nums, L, m)
        root.right = SegmentNode.build(nums, m+1, R)
        root.total = root.left.total + root.right.total
        return root
    
    def update(self, index, val):
        if self.li == self.ri:
            self.total = val
            return 

        m = (self.li + self.ri)//2
        if index > m:
            self.right.update(index, val)
        else:
            self.left.update(index, val)
        self.total = self.left.total + self.right.total

    def query(self, L, R):
        if L == self.li and self.ri == R:
            return self.total

        m = (self.li + self.ri)//2
        if L > m:
            return self.right.query(L, R)
        elif R <= m:
            return self.left.query(L, R)
        else:
            return self.left.query(L, m) + self.right.query(m+1, R)

class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self.root = SegmentNode.build(nums, 0, len(nums)-1)
    
    def update(self, index: int, val: int) -> None:
        self.root.update(index, val)
    
    def query(self, L: int, R: int) -> int:
        return self.root.query(L, R)
