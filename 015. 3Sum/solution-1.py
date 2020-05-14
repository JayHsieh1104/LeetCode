class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
                
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            target = 0 - nums[i]
            pointer1 = i + 1
            pointer2 = len(nums) - 1
            while pointer1 < pointer2:
                if nums[pointer1] + nums[pointer2] == target:
                    res.append([nums[i], nums[pointer1], nums[pointer2]])     
                    while pointer1 < pointer2 and nums[pointer1] == nums[pointer1 + 1]:
                        pointer1 += 1
                    while pointer1 < pointer2 and nums[pointer2] == nums[pointer2 - 1]:
                        pointer2 -= 1
                    pointer1 += 1
                    pointer2 -= 1
                elif nums[pointer1] + nums[pointer2] < target:
                    pointer1 += 1
                else:
                    pointer2 -= 1
                   
        return res