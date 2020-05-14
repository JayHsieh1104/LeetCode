class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        
        total_fresh_orange = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    total_fresh_orange += 1
        prev_round_fresh_organge = total_fresh_orange
        counter = 0
        
        while total_fresh_orange != 0:
            counter += 1
            for y in range(len(grid)):
                for x in range(len(grid[0])):
                    if grid[y][x] == 2:
                        if y - 1 >= 0 and grid[y-1][x] == 1:
                            grid[y-1][x] = -2
                        if y + 1 < len(grid) and grid[y+1][x] == 1:
                            grid[y+1][x] = -2
                        if x - 1 >= 0 and grid[y][x-1] == 1:
                            grid[y][x-1] = -2
                        if x + 1 < len(grid[0]) and grid[y][x+1] == 1:
                            grid[y][x+1] = -2

            for y in range(len(grid)):
                for x in range(len(grid[0])):
                    if grid[y][x] == -2:
                        grid[y][x] = 2
                        total_fresh_orange -= 1
                        
            if total_fresh_orange == prev_round_fresh_organge:
                break
            else:
                prev_round_fresh_organge = total_fresh_orange
        
        if total_fresh_orange == 0:
            return counter
        else:
            return -1