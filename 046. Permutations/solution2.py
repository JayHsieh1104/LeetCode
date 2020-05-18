class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtracking(level=0):
            if level == len(nums):
                ret.append(solution[:])
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    solution[level] = nums[i]
                    backtracking(level+1)
                    used[i] = False
        
        used = [False] * len(nums)
        solution = [0] * len(nums)
        ret = []
        backtracking()
        
        return ret