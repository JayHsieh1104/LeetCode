class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:   
        def backtracking(start_position, remaining, currentList):
            if remaining == 0:
                ret.append(currentList[:])
                return

            for i in range(start_position, len(candidates)):
                if candidates[i] > remaining:
                    break
                else:
                    backtracking(i, remaining - candidates[i], currentList + [candidates[i]])
        
        candidates.sort()
        ret = []
        backtracking(0, target, [])
        return ret