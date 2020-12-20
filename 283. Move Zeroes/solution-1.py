class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_counter = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_counter += 1
            else:
                if zero_counter > 0:
                    nums[i - zero_counter], nums[i] = nums[i], nums[i - zero_counter]
