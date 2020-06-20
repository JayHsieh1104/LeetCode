class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        curMaxArea = 0
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
          
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == '0':
                    continue
                if j != 0:
                    curWidth = dp[i][j] = dp[i][j-1] + 1
                else:
                    curWidth = dp[i][j] = 1
                for k in range(i, -1, -1):
                    if dp[k][j] == 0:
                        break
                    curWidth = min(curWidth, dp[k][j])
                    curMaxArea = max(curMaxArea, curWidth * (i - k + 1))
        return curMaxArea