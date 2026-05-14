class Solution:

    def rate_check(self, piles, rate, h):
        p = 0
        i = 0
        while p <= h:
        
            if i >= len(piles):
                return True
            k = piles[i] 
            if k % rate == 0:
                t = k//rate
            else:
                t = (k//rate) +1
            p += t
            i += 1
            print(p, t, k, i, rate)
        return False

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        
        min_rate = r

        while l <=r :
            m = (l+r)//2
            t = self.rate_check(piles, m, h)

            if t:
                r = m-1
                min_rate = min(min_rate, m)
                
            else:
                l = m+1
            print(l, r, min_rate, t, piles)
        return min_rate