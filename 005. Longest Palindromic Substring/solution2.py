class Solution:
    def longestPalindrome(self, s: str) -> str:   
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        max_length = 1
        start = 0

        for i in range(n):
            dp[i][i] = 1
            for j in range(i):
                if s[j] == s[i] and (dp[j+1][i-1] > 0 or i - j == 1) :
                    dp[j][i] = dp[j+1][i-1] + 2
                    if dp[j][i] > max_length:
                        max_length = dp[j][i]
                        start = j

        return s[start : start + max_length]