class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()

        def area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0]) and (r, c) not in visited and grid[r][c]):
                return 0
            visited.add((r, c))
            return (1 + area(r-1, c) + area(r+1, c) + area(r, c-1) + area(r, c+1))

        return max(area(r, c) for r in range(len(grid)) for c in range(len(grid[0])))
