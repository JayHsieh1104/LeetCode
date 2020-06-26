class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        isRemoved = set()
        leftParentheseCounter = rightParentheseCounter = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                leftParentheseCounter += 1
            elif s[i] == ')':
                rightParentheseCounter += 1
            if rightParentheseCounter > leftParentheseCounter:
                isRemoved.add(i)
                rightParentheseCounter -= 1
            
        diff = leftParentheseCounter - rightParentheseCounter
        pointer = len(s) - 1
        while diff > 0:
            if s[pointer] == '(':
                isRemoved.add(pointer)
                diff -= 1
            pointer -= 1
            
        ret = ''
        for i in range(len(s)):
            if i not in isRemoved:
                ret += s[i]
            
        return ret