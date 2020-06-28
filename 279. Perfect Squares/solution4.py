class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if nums.count(1) == n:
            return n - 1

        i = currLength = maxLength = 0
        for j in range(n):
            if nums[j] == 1:
                currLength += 1
                if currLength > maxLength:
                    maxLength = currLength
            while j - i > currLength:
                if nums[i] == 1:
                    currLength -= 1
                i += 1
        
        return maxLength