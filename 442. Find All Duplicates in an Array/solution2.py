class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = set(nums)
        res = []
        
        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                res.append(num)
                
        return res