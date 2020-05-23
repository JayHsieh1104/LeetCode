class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        P1 = 0
        P2 = len(string) - 1
        
        while P1 < P2:
            if string[P1] != string[P2]:
                return False
            P1 += 1
            P2 -= 1
            
        return True