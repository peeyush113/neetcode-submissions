class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        l, r = 0, len(heights)-1

        while l < r:
            hr = heights[r]
            hl = heights[l]
            maxWater = max(maxWater, min(hr, hl)*(r-l))
            if hr > hl:
                l += 1
            else:
                r -=1 
        
        return maxWater