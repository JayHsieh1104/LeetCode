import queue

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ret = 0
        if not grid:
            return ret
        
        for mY in range(len(grid)):
            for mX in range(len(grid[0])):
                if grid[mY][mX] == '1':
                    grid[mY][mX] = '0'
                    q = queue.Queue()
                    q.put((mY, mX))
                    ret += 1
                    while(not q.empty()):
                        y, x = q.get()
                        if y - 1 >= 0 and grid[y-1][x] == '1':
                            q.put((y-1, x))
                            grid[y-1][x] = '0'
                        if y + 1 < len(grid) and grid[y+1][x] == '1':
                            q.put((y+1, x))
                            grid[y+1][x] = '0'
                        if x - 1 >= 0 and grid[y][x-1] == '1':
                            q.put((y, x-1))
                            grid[y][x-1] = '0'
                        if x + 1 < len(grid[0]) and grid[y][x+1] == '1':
                            q.put((y, x+1))
                            grid[y][x+1] = '0'
        return ret