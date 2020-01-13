class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        
        if not grid:
            return res
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.DFS_searching(grid, i, j)
                    res += 1
        return res
    
    def DFS_searching(self, grid, i, j) -> None:
        if (i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0])) or grid[i][j] == '0':
            return
        
        grid[i][j] = '0'
        self.DFS_searching(grid, i-1, j)
        self.DFS_searching(grid, i+1, j)
        self.DFS_searching(grid, i, j-1)
        self.DFS_searching(grid, i, j+1)