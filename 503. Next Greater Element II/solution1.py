class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        descending_stack = []
        ret = [-1] * len(nums)
        
        for i in range(2*len(nums)):
            while descending_stack and nums[i%len(nums)] > nums[descending_stack[-1]]:
                if descending_stack[-1] < len(nums):
                    ret[descending_stack[-1]] = nums[i%len(nums)]
                descending_stack.pop()
            descending_stack.append(i%len(nums))
        
        return ret