class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        poppedItemCounter = 0
        stack = []
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[poppedItemCounter]:
                stack.pop()
                poppedItemCounter += 1
                
        return poppedItemCounter == len(popped)