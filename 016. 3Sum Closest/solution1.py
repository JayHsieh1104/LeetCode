class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ret = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if abs(nums[i]+nums[j]+nums[k] - target) < abs(ret - target):
                        ret = nums[i]+nums[j]+nums[k]
        return ret