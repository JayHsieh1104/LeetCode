class Solution:
    def numTrees(self, n: int) -> int:
        self.memo = {}
        def getNum(start: int, end: int) -> int:           
            ans = 0
            if start >= end:
                return 1
            elif (start, end) in self.memo:
                return self.memo[(start, end)]
            
            for i in range(start, end+1):
                left_subtree = getNum(start, i-1)
                right_subtree = getNum(i+1, end)
                ans += left_subtree * right_subtree
                
            self.memo[(start, end)] = ans
            return ans
        return getNum(1, n)