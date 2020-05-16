class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        
        for num in nums:
            ret += [subset + [num] for subset in ret]
        
        return ret