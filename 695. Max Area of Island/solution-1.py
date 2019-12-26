class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        maximum_area = 0
        
        for r0, row in enumerate(grid):
            for c0, val in enumerate(row):
                if val and (r0, c0) not in visited:
                    shape = 0
                    stack = [(r0, c0)]
                    visited.add((r0, c0))
                    while stack:
                        r, c = stack.pop()
                        shape += 1
                        for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                            if (0 <= nr < len(grid) and 0 <= nc < len(grid[0])
                                and grid[nr][nc] and (nr, nc) not in visited):
                                stack.append((nr, nc))
                                visited.add((nr, nc))
                    maximum_area = max(maximum_area, shape)
                    
        return maximum_area