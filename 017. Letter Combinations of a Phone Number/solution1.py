class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_length = len(digits)
        mDict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        def backtracking(combination='', current_position=0):
            if len(combination) == digits_length:
                res.append(combination)
                return
            
            for letter in mDict[digits[current_position]]:
                backtracking(combination+letter, current_position+1)
        
        res = []
        if digits:
            backtracking()
        
        return res