class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        curMaxArea = 0
        dp = [0] * (len(matrix[0]) + 1)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == '0':
                    dp[j] = 0
                    continue
                if i != 0:
                    dp[j] = dp[j] + 1
                else:
                    dp[j] = 1
                    
            ascending_stack = [-1]
            for j in range(len(dp)):
                while dp[ascending_stack[-1]] > dp[j]:
                    curMaxArea = max(curMaxArea, dp[ascending_stack.pop()] * (j - 1 - ascending_stack[-1]))
                ascending_stack.append(j)
            
        return curMaxArea