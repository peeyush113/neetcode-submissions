class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval
        res = []
        for i in range(len(intervals)):
            x, y = intervals[i]
            if end < x:
                res.append([start, end])
                return res + intervals[i:]
            elif start > y:
                res.append([x, y])
            else:
                start = min(start, x) 
                end = max(end, y)
        res.append([start, end])
        return res
               
