class Solution:
    def sortColors(self, nums: List[int]) -> None:
        rightMostOfZero = curr = 0
        leftMostOfTwo = len(nums) - 1
        
        while curr <= leftMostOfTwo:
            if nums[curr] == 0:
                nums[curr], nums[rightMostOfZero] = nums[rightMostOfZero], nums[curr]
                curr += 1
                rightMostOfZero += 1
            elif nums[curr] == 2:
                nums[curr], nums[leftMostOfTwo] = nums[leftMostOfTwo], nums[curr]
                leftMostOfTwo -= 1
            else:
                curr += 1