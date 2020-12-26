class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        def calculateArea(lo, hi):
            if lo > hi:
                return 0
            else:
                min_height_pos = lo
                for i in range(lo + 1, hi + 1):
                    if heights[i] < heights[min_height_pos]:
                        min_height_pos = i
                return max(heights[min_height_pos] * (hi - lo + 1), calculateArea(lo, min_height_pos - 1), calculateArea(min_height_pos + 1, hi))

        return calculateArea(0, len(heights) - 1)
