class Solution:
    def isHappy(self, n: int) -> bool:
        
        def getNext(n: int) -> int:
            next_num = 0
            while n > 0:
                next_num += (n % 10) ** 2
                n = n // 10  
            return next_num
        
        seen = set()
        while n != 1 and n not in seen: 
            seen.add(n)
            n = getNext(n)
        
        return n == 1