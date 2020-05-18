class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(currList=[], first=0):
            if len(currList) == n:
                ret.append(currList[:])
                return

            for i in range(first, len(nums)):
                if i > first and nums[i] == nums[i-1]:
                    continue
                currList.append(nums[i])
                backtrack(currList, i+1)
                currList.pop()
        
        ret = []
        nums.sort()
        for n in range(len(nums)+1):
            backtrack()
        
        return ret