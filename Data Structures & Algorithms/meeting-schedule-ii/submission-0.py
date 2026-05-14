"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        days = 0
        intervals.sort(key=lambda x: x.start)
        # print([[i.start, i.end] for i in intervals])
        while intervals:
            days += 1
            
            pe = intervals.pop(0)
            for i in range(1, len(intervals)+1):
                interval = intervals.pop(0)
                print(pe.start, pe.end, interval.start, interval.end)
                if interval.start<pe.end:
                    intervals.append(interval)
                else:
                    pe = interval
            # print([[i.start, i.end] for i in intervals])
        return days