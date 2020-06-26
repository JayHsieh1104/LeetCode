class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        isRemoved = set()
        stack = []
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    isRemoved.add(i)
        
        if stack:
            while stack:
                isRemoved.add(stack.pop())
            
        ret = ''
        for i in range(len(s)):
            if i not in isRemoved:
                ret += s[i]
            
        return ret