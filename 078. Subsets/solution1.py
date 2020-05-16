class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtracking(n: int):
            if n == len(nums):
                subset = []
                for i in range(len(nums)):
                    if used[i] == 1:
                        subset.append(nums[i])
                res.append(subset)
                return
            
            used[n] = 1
            backtracking(n+1)

            used[n] = 0
            backtracking(n+1)
        
        res = []
        used = [0] * len(nums)
        backtracking(0)
        return res