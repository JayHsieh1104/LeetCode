class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        def calculateArea(start, end):
            if start > end:
                return 0
            
            min_height_pos = start
            for i in range(start, end+1):
                if heights[i] < heights[min_height_pos]:
                    min_height_pos = i
            return max(heights[min_height_pos] * (end - start + 1), calculateArea(start, min_height_pos-1), calculateArea(min_height_pos+1, end))
        
        return calculateArea(0, len(heights)-1)