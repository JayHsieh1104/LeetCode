class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ret = 0
        for i in range(len(heights)):
            min = heights[i]
            for j in range(i, len(heights)):
                if heights[j] < min:
                    min = heights[j]
                if min * (j-i+1) > ret:
                    ret = min * (j-i+1)
        return ret