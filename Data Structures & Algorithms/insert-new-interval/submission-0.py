class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        resp = []
        start = newInterval[0]
        end = newInterval[1]
        for i in range(len(intervals)):        
            s = intervals[i][0]
            e = intervals[i][1]
            if end<s:
                resp.append([start, end])
                return resp+intervals[i:]
            elif start>e:
                resp.append([s, e])
            else:
                start = min(start, s)
                end = max(end, e)
        resp.append([start, end])
        return resp            

