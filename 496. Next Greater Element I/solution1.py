class Solution:  
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ret = []
        greaterSet = {}
        descending_stack = []
        
        for num in nums2:
            while descending_stack and num > descending_stack[-1]:
                greaterSet[descending_stack[-1]] = num
                descending_stack.pop()
            descending_stack.append(num)
        
        for num in nums1:
            if num in greaterSet:
                ret.append(greaterSet[num])
            else:
                ret.append(-1)
            
        return ret