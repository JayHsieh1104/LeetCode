class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = right_max = 0
        left_pointer = 0
        right_pointer = len(height) - 1
        sum = 0
        
        while left_pointer <= right_pointer:
            if left_max > right_max:
                if height[right_pointer] >= right_max:
                    right_max = height[right_pointer]
                else:
                    sum += right_max - height[right_pointer]
                right_pointer -= 1
            else:
                if height[left_pointer] >= left_max:
                    left_max = height[left_pointer]
                else:
                    sum += left_max - height[left_pointer]
                left_pointer += 1
        return sum