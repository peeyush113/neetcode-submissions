class Solution:
    def trap(self, height: List[int]) -> int:
        # O(n) mem solution

        maxLeft = []
        ml = 0
        for n in height:
            maxLeft.append(ml)
            ml = max(ml, n)
            
        maxRight = [0]*len(height)
        mr = 0
        for i in range(len(height)-1, 0, -1):
            maxRight[i] = mr
            n = height[i]
            mr = max(mr, n)
            
        
        maxWater = 0
        for i in range(len(height)):
            h = min(maxLeft[i], maxRight[i])-height[i]
            if h < 0:
                h = 0
            
            maxWater += h
        return maxWater