class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        area = 0
        while l<r:
            hl, hr = heights[l], heights[r]
            curr_area = min(hl, hr)*(r-l)
            area = max(area, curr_area)
            print(l, r, hl, hr, curr_area, area)
            if hl < hr:
                l += 1
            else:
                r -= 1
            
        return area