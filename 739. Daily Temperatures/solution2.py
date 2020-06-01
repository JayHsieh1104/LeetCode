from collections import defaultdict
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        descending_stack = []
        ret = [0] * len(T)
        
        for i in range(0, len(T)):
            while descending_stack and T[descending_stack[-1]] < T[i]:
                ret[descending_stack[-1]] = i - descending_stack[-1]
                descending_stack.pop()
            descending_stack.append(i)
        return ret