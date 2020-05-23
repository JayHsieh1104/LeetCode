class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        stack = []
        x_copy = x
        
        while x_copy > 0:
            stack.append(x_copy % 10)
            x_copy //= 10
        
        for i in range(len(stack)):
            x_copy += stack.pop() * (10**i)
        
        if x == x_copy:
            return True
        else:
            return False