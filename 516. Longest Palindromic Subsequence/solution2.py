class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        for j in range(n):
            preservedLeftRightNum = dp[j]
            dp[j] = 1
            for i in range(j-1, -1, -1):
                temp = dp[i]
                if s[i] == s[j]:
                    dp[i] = preservedLeftRightNum + 2
                else:
                    dp[i] = max(dp[i], dp[i+1])
                preservedLeftRightNum = temp
        return dp[0]