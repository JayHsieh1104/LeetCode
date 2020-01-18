class Solution:
    res = 0
    def countSubstrings(self, s: str) -> int:
        for i in range(len(s)):
            self.helper(s, i, i+1)
            self.helper(s, i, i)
        return self.res
            
    def helper(self, s: str, i: int, j: int) -> None:
        while i >= 0 and j < len(s) and s[i] == s[j]:
            self.res += 1
            i -= 1
            j += 1