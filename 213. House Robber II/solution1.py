class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        prev1 = curr1 = prev2 = curr2 = 0
        for i in range(len(nums)-1):
            prev1, curr1 = curr1, max(curr1, prev1+nums[i])
        for i in range(1, len(nums)):
            prev2, curr2 = curr2, max(curr2, prev2+nums[i])
            
        return max(curr1, curr2)