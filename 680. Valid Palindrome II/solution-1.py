class Solution:
    def validSubPalindrome(self, pointer1: int, pointer2: int, s: str) -> bool:
        while pointer1 < pointer2:
            if s[pointer1] != s[pointer2]:
                return False
            else:
                pointer1 += 1
                pointer2 -= 1
        return True
        
    def validPalindrome(self, s: str) -> bool:
        pointer1 = 0
        pointer2 = len(s) - 1
        
        while pointer1 < pointer2:
            if s[pointer1] == s[pointer2]:
                pointer1 += 1
                pointer2 -= 1
            else:
                if self.validSubPalindrome(pointer1+1, pointer2, s) or \
                self.validSubPalindrome(pointer1, pointer2-1, s):
                    return True
                else:
                    return False
        return True