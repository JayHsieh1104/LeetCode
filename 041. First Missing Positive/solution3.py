class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        is_one_existed = False
        for i in range(len(nums)):
            if nums[i] == 1:
                is_one_existed = True
            elif nums[i] > len(nums) or nums[i] < 1:
                nums[i] = 1
        if not is_one_existed:
            return 1

        for i in range(len(nums)):
            if nums[abs(nums[i])-1] > 0:
                nums[abs(nums[i])-1] = -1 * nums[abs(nums[i])-1]

        for i in range(len(nums)):
            if nums[i] > 0:
                return i+1
        return len(nums)+1
