class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        def eatingTime(rate):
            hours = 0
            for p in piles:
                hours += p//rate
                hours += 1 if p%rate else 0
                # print(rate, hours)
            return hours
        
        l, r, rate = 1, piles[-1], 0
        while l<=r:
            m = (l+r)//2
            eating_hours = eatingTime(m)
            if eating_hours > h:
                l = m+1
            else:
                r = m-1
                rate = m

            print(l, r, piles, h, rate, eating_hours, m)    
        
        return rate