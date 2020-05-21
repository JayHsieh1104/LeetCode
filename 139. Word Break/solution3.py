class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def helper(substring: str) -> bool:
            if DP[len(substring)] != -1:
                return DP[len(substring)]
            
            for i in range(len(substring)):
                if helper(substring[:i]) and substring[i:] in wordDict:
                    DP[len(substring)] = True
                    return True
            DP[len(substring)] = False
            return False
        
        DP = [-1] * (len(s) + 1)
        DP[0] = True
        return helper(s)