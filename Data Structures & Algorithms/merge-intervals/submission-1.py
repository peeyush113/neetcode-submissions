class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        resp = []
        intervals.sort(key=lambda x: x[0])
        start = intervals[0][0]
        end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            s, e = intervals[i][0], intervals[i][1]

            if end<s:
                resp.append([start, end])
                start, end = s, e
            else:
                start, end = min(s, start), max(e, end)
        resp.append([start, end])
        return resp