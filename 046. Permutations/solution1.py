class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        
        def backtracking(first_index: int):
            if first_index == len(nums) - 1:
                ret.append(nums[:])
                return
            
            for i in range(first_index, len(nums)):
                nums[first_index], nums[i] = nums[i], nums[first_index]
                backtracking(first_index+1)
                nums[i], nums[first_index] = nums[first_index], nums[i]
        
        backtracking(0)
        return ret