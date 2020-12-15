class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        dp = [[None] * len(s) for _ in range(len(s))]
        
        def is_palindrome(i, j) -> bool:
            if i+1 <= j-1 and dp[i+1][j-1] != None:
                return dp[i+1][j-1] and s[i] == s[j]
            else:
                if s[i:j+1] == "".join(reversed(s[i:j+1])):
                    dp[i][j] = True
                    return True
                else:
                    dp[i][j] = False
                    return False
                
        def dfs(current_list = [], start_index = 0):
            if start_index == len(s):
                res.append(current_list[:])
                return
            for i in range(start_index, len(s)):
                if is_palindrome(start_index, i):
                    current_list.append(s[start_index:i+1])
                    dfs(current_list, i+1)
                    current_list.pop()       
            
        dfs()
        return res