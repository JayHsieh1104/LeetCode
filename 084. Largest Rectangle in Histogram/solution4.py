class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        ascending_stack = [-1]
        max_area = 0
        
        for i in range(len(heights)):
            while heights[i] < heights[ascending_stack[-1]]:
                max_area = max(max_area, heights[ascending_stack.pop()] * (i - 1 - ascending_stack[-1]))
            ascending_stack.append(i)
            
        return max_area