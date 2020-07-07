class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        stack = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    stack.append((i, j))
                    break
            if len(stack) == 1:
                break
                    
        perimeter = 0
        while stack:
            y, x = stack.pop()
            grid[y][x] = -1
            perimeter += 4
            for new_y, new_x in [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]:
                if new_y >= 0 and new_y < len(grid) and new_x >= 0 and new_x < len(grid[0]):
                    if grid[new_y][new_x] != 0:
                        perimeter -= 1
                    if grid[new_y][new_x] == 1:
                        if (new_y, new_x) not in stack:
                            stack.append((new_y, new_x))
        
        return perimeter