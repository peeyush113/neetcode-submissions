class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        area = 0

        for i in range(len(heights)):
            while stack[-1]  != -1 and heights[stack[-1]] >= heights[i]:
                height = heights[stack.pop()]
                width = i - stack[-1] -1
                area = max(area, height*width)
            stack.append(i)
        while stack[-1] != -1:
            height = heights[stack.pop()]
            width = len(heights) - stack[-1] -1
            area = max(area, height*width)
        return area