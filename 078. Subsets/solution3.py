class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ret = []
        
        for i in range(2**n, 2**(n+1)):
            bitmask = bin(i)[3:]
            temp = []
            for j in range(len(nums)):
                if bitmask[j] == '1':
                    temp += [nums[j]]
            ret += [temp]
        
        return ret