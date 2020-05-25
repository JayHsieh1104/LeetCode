class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left = 0
        sum = 0
        minLen = sys.maxsize
        
        for i in range(len(nums)):
            sum += nums[i]
            while(sum >= s):
                minLen = min(minLen, i-left+1)
                sum -= nums[left]
                left += 1
                
        if minLen == sys.maxsize:
            return 0
        else:
            return minLen