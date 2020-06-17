class Solution:
    def rob(self, nums: List[int]) -> int:
        prevMax = 0
        currMax = 0
        for num in nums:
            temp = max(currMax, prevMax + num)
            prevMax, currMax = currMax, temp
        
        return currMax