class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        dp = []
        for i in range(n):
            dp.append(nums[i])
            for j in range(i + 1, n):
                dp.append(dp[-1] + nums[j])
            if len(dp) > (n * (n+1) / 2):
                break

        dp.sort()

        _sum = 0
        for i in range(left - 1, right):
            _sum += dp[i]

        return _sum