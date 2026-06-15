class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        end = intervals[0][1]
        count = 0
        for x, y in intervals[1:]:
            if x>=end:
                end = y 
            else:
                end = min(end, y)
                count += 1
        return count
