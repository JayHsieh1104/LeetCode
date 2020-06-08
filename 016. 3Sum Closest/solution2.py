class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ret = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
            pointer1 = i + 1
            pointer2 = len(nums) - 1
            while pointer1 < pointer2:
                if abs(nums[i]+nums[pointer1]+nums[pointer2]-target) < abs(ret-target):
                    ret = nums[i]+nums[pointer1]+nums[pointer2]
                    
                if nums[i]+nums[pointer1]+nums[pointer2] > target:
                    pointer2 -= 1
                else:
                    pointer1 += 1
        return ret