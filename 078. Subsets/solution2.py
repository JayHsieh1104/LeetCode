class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        for num in nums:
            current_length = len(res)
            for i in range(current_length):
                if (res[i] + [num]) not in res:
                    res.append(res[i] + [num])
        return res