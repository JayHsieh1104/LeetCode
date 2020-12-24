class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        else:
            ret = nums[0]
            
            for i in range(len(nums)):
                accumulator = 1
                for j in range(i, len(nums)):
                    accumulator *= nums[j]
                    ret = max(ret, accumulator)
                    
        return ret