class Solution:
    def isHappy(self, n: int) -> bool:
        
        def getNext(n: int) -> int:
            next_num = 0
            while n > 0:
                next_num += (n % 10) ** 2
                n = n // 10  
            return next_num
        
        slow_runner = n
        fast_runner = getNext(n)
        while fast_runner != 1 and slow_runner != fast_runner: 
            slow_runner = getNext(slow_runner)
            fast_runner = getNext(getNext(fast_runner))
        
        return fast_runner == 1