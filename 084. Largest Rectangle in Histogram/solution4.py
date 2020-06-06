class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
  
        ret = 0
        ascending_stack = [-1]
        heights.append(0)
        
        for i in range(len(heights)):
            while heights[ascending_stack[-1]] > heights[i]:
                ret = max(ret, heights[ascending_stack.pop()] * (i - 1 - ascending_stack[-1]))
            ascending_stack.append(i)
        
        heights.pop()
        return ret