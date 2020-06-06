class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ret = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                min = heights[i]
                for k in range(i+1, j+1):
                    if heights[k] < min:
                        min = heights[k]
                if min * (j-i+1) > ret:
                    ret = min * (j-i+1)
        return ret