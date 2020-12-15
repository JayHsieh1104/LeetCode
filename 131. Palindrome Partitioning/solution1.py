class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def is_palindrome(word: str) -> bool:
            if word == word[::-1]:
                return True
            else:
                return False
                
        def dfs(current_list = [], start_index = 0):
            if start_index == len(s):
                res.append(current_list[:])
                return
            for i in range(start_index, len(s)):
                if is_palindrome(s[start_index:i+1]):
                    current_list.append(s[start_index:i+1])
                    dfs(current_list, i+1)
                    current_list.pop()       
            
        dfs()
        return res