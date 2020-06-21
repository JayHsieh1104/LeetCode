class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def doPermutation(currentString):
            if len(currentString) == n:
                self.count += 1
                self.ret = currentString
                return
            
            for i in range(1, n+1):
                if self.used[i]:
                    continue
                    
                self.used[i] = True
                doPermutation(currentString + str(i))
                if self.count == k:
                    return
                self.used[i] = False
        
        self.count = 0
        self.ret = ''
        self.used = [False] * (n+1)
        doPermutation('')
        
        return self.ret