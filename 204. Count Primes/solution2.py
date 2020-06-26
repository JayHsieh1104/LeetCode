class Solution:
    def validSubPalindrome(self, i: int, j: int, s: str) -> bool:
        return all(s[k] == s[j-k+i] for k in range(i, j))
        
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s) // 2):
            if s[i] != s[-1-i]:
                j = len(s) - 1 - i
                return self.validSubPalindrome(i+1, j, s) or self.validSubPalindrome(i, j-1, s)
        return True