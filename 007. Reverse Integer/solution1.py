class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2 ** 31 - 1
        MIN = -2 ** 31
        if x > MAX or x < MIN:
            return 0
        
        isPositive = x > 0
        if not isPositive:
            x *= -1
        
        reversed_x = 0
        while x > 0:
            reversed_x = 10 * reversed_x + x % 10
            if reversed_x > MAX:
                return 0
            x //= 10
        
        if not isPositive:
            return reversed_x * -1
        else:
            return reversed_x