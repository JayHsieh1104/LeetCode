class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = [0]
        for i in range(len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])
        
        counter = 0
        for i in range(len(nums), 0, -1):
            for j in range(i):
                if (prefix_sum[i] - prefix_sum[j]) == k:
                    counter += 1
        return counter