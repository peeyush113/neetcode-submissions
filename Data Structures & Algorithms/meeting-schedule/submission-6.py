"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        if not intervals:
            return True

        print([(i.start, i.end) for i in intervals])
        prev = intervals[0]
        for curr in intervals[1:]:
            if curr.start < prev.end:
                return False
            prev = curr
        return True
