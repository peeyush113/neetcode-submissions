class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        resp = 0
        pe = intervals[0][1]

        for start, end in intervals[1:]:
            if start>=pe:
                pe = end
            else:
                resp += 1
                pe = min(end, pe)
        return resp