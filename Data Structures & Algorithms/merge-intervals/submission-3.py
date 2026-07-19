class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        res = []
        start, end = intervals[0]
        for x, y in intervals[1:]:
            if end < x:
                res.append([start, end])
                start, end = x, y
            else:
                start = min(start, x)
                end = max(end, y)
        res.append([start, end])
        return res