class Solution:
    def trap(self, height: List[int]) -> int:
        leftLimitPos = 0
        rightLimitPos = len(height) - 1
        pointer1 = 0
        pointer2 = len(height) - 1
        totalWater = 0

        while pointer1 < pointer2:
            if height[leftLimitPos] < height[rightLimitPos]:
                pointer1 += 1
                if height[pointer1] < min(height[leftLimitPos], height[rightLimitPos]):
                    totalWater += min(height[leftLimitPos], height[rightLimitPos]) - height[pointer1]
                if height[pointer1] > height[leftLimitPos]:
                    leftLimitPos = pointer1
            else:
                pointer2 -= 1
                if height[pointer2] < min(height[leftLimitPos], height[rightLimitPos]):
                    totalWater += min(height[leftLimitPos], height[rightLimitPos]) - height[pointer2]
                if height[pointer2] > height[rightLimitPos]:
                    rightLimitPos = pointer2
                    
        return totalWater