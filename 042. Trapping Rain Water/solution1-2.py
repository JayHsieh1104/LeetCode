class Solution:
    def trap(self, height: List[int]) -> int:
        if len (height) < 3:
            return 0
        else:
            left_max = [0] * len(height)
            left_max[0] = height[0]
            right_max = [0] * len(height)
            right_max[-1] = height[-1]

            for i in range(1, len(height)):
                if height[i] > left_max[i-1]:
                    left_max[i] = height[i]
                else:
                    left_max[i] = left_max[i-1]

            for i in range(len(height)-2, -1, -1):
                if height[i] > right_max[i+1]:
                    right_max[i] = height[i]
                else:
                    right_max[i] = right_max[i+1]

            sum = 0

            for i in range(1, len(height)-1):
                sum += min(left_max[i], right_max[i]) - height[i]                                  

            return sum