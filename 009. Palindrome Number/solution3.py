class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        revertedNum = 0
        while revertedNum < x:
            revertedNum = revertedNum * 10 + x % 10
            x //= 10
            
        if x == revertedNum or x == revertedNum // 10:
            return True
        else:
            return False