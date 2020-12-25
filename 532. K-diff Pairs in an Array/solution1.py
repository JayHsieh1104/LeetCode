class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        result = 0
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            for j in range(i+1, len(nums)):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue

                if nums[j] - nums[i] == k:
                    result += 1
        
        return result