class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def daysTaken(capacity):
            prev, day = 0, 0
            for w in weights:
                if prev+w>capacity:
                    day += 1
                    prev = w
                else:
                    prev += w
            return day
        
        l, r, cap = max(weights), sum(weights), 0
        while l<=r:
            m = (l+r)//2
            op = daysTaken(m)
            if op < days:
                r = m-1
                cap = m
            else:
                l = m+1
        return cap

