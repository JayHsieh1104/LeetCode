class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def DFS(remain_string: str) -> bool:
            if remain_string in memo:
                return memo[remain_string]
            
            if remain_string == '#' * len(s):
                return True
            
            ret = False
            for word in wordDict:
                if word in remain_string:
                    space = '#' * len(word)
                    ret = DFS(remain_string.replace(word, space))
                    memo[remain_string.replace(word, space)] = False
                if ret:
                    break
            return ret
        memo = {}
        return DFS(s)