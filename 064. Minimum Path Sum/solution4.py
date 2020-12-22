class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for row in range(len(grid)-1, -1, -1):
            for col in range(len(grid[0])-1, -1, -1):
                if row != len(grid)-1 and col != len(grid[0])-1:
                    grid[row][col] = grid[row][col] + \
                        min(grid[row+1][col], grid[row][col+1])
                elif row == len(grid)-1 and col != len(grid[0])-1:
                    grid[row][col] = grid[row][col] + grid[row][col+1]
                elif row != len(grid)-1 and col == len(grid[0])-1:
                    grid[row][col] = grid[row][col] + grid[row+1][col]

        return grid[0][0]
