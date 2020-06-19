class Solution:
    def longestPalindrome(self, s: str) -> str:
        def searchLongestPalindrome(left, right):
            if left < self.subStringLen // 2 or self.n - right < self.subStringLen // 2:
                return
            while left > 0 and right < self.n - 1 and s[left - 1] == s[right + 1]:
                left -= 1
                right += 1
            if right - left + 1 > self.subStringLen:
                self.subStringLen = right - left + 1
                self.start = left
        
        self.n = len(s)
        self.start = self.subStringLen = 0
        
        for i in range(self.n - 1):
            searchLongestPalindrome(i, i)
            if s[i] == s[i+1]:
                searchLongestPalindrome(i, i + 1)
        searchLongestPalindrome(self.n - 1, self.n - 1)
    
        return s[self.start : self.start + self.subStringLen]