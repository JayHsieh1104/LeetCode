class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:      
        def DFS(cur_string: str) -> bool:
            if cur_string in memo:
                return memo[cur_string]
            
            if len(cur_string) > len(s):
                return False

            if len(cur_string) == len(s):
                if cur_string == s:
                    return True
                else:
                    return False
            
            for i in range(len(cur_string)):
                if cur_string[i] != s[i]:
                    return False
            
            for word in wordDict:
                if DFS(cur_string+word):
                    memo[cur_string] = True
                    return True

            memo[cur_string] = False
            return False
        
        memo = {}
        return DFS('')