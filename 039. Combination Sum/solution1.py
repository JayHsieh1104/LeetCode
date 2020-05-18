class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:   
        def backtrack(remain, cur_list):           
            if remain == 0:
                ret.append(cur_list)
                return

            for item in candidates:
                if item > remain:
                    break
                if cur_list and cur_list[-1] > item:
                    continue
                backtrack(remain-item, cur_list+[item])

        candidates.sort()
        ret = []
        backtrack(target, [])
        
        return ret