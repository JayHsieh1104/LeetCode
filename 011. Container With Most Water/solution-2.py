class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1, p2 = 0, len(height) - 1
        max_num = 0
        
        while p1 < p2:
            if height[p1] < height[p2]:
                if height[p1] * (p2-p1) > max_num:
                    max_num = height[p1] * (p2-p1)
                p1 += 1
            else:
                if height[p2] * (p2-p1) > max_num:
                    max_num = height[p2] * (p2-p1)
                p2 -= 1
        
        return max_num