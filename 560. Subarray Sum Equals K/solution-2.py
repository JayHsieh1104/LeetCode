class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            sub_sum = 0
            for j in range(i, len(nums)):
                sub_sum += nums[j]
                if sub_sum == k:
                    count += 1
        return count