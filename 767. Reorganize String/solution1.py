class Solution:
    def reorganizeString(self, S: str) -> str:
        
        def backtrack(cur_string: str) -> None:
            if len(cur_string) == len(S):
                self.ret += cur_string
                self.isFound = True
                return
            
            for i in range(len(S)):
                if not used[i] and (len(cur_string) == 0 or S[i] != cur_string[-1]):
                    used[i] = True
                    backtrack(cur_string + S[i])
                    if self.isFound:
                        break
                    used[i] = False
        
        self.isFound = False
        self.ret = ''
        used = [False] * len(S)
        backtrack('')
        return self.ret