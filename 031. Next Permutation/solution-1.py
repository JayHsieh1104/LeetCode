class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        turning_position = len(nums) - 2
        while turning_position > -1 and nums[turning_position] >= nums[turning_position+1]:
            turning_position -= 1
        
        if turning_position == -1:
            nums.reverse()
            return
        else:
            exchanged_position = len(nums) - 1
            while turning_position < exchanged_position and nums[turning_position] >= nums[exchanged_position]:
                exchanged_position -= 1
        nums[turning_position], nums[exchanged_position] = nums[exchanged_position], nums[turning_position]
        nums[turning_position+1:] = reversed(nums[turning_position+1:])
        return