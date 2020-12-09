class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []
        
        if len(nums) == 0:
            if lower == upper:
                return [str(lower)]
            else:
                return [str(lower) + "->" + str(upper)]
        else:
            if lower < nums[0]:
                if nums[0] - lower == 1:
                    res.append(str(lower))
                else:
                    res.append(str(lower) + "->" + str(nums[0]-1))
        
            for i in range(len(nums) - 1):
                if nums[i+1] - nums[i] == 2:
                    res.append(str(nums[i]+1))
                elif nums[i+1] - nums[i] > 2:
                    res.append(str(nums[i]+1) + "->" + str(nums[i+1]-1))
                    
            if nums[-1] < upper:
                if upper - nums[-1] == 1:
                    res.append(str(upper))
                else:
                    res.append(str(nums[-1]+1) + "->" + str(upper))
        
        return res