class SegmentNode:

    def __init__(self, li, ri) -> None:
        self.li, self.ri = li, ri
        self.left, self.right = None, None
    
    def insert_event(self, li, ri):
        if ri <= self.li:
            if not self.left:
                self.left = SegmentNode(li, ri)
                return True
            return self.left.insert_event(li, ri)
        elif li >= self.ri:
            if not self.right:
                self.right = SegmentNode(li, ri)
                return True
            return self.right.insert_event(li, ri)
        else:
            return False

class MyCalendar:
    
    def __init__(self):
        self.root = None

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.root:
            self.root = SegmentNode(startTime, endTime)
            return True
        
        return self.root.insert_event(startTime, endTime)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)