class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                curr_area = 0
                stack = []
                if grid[row][col] == 1:
                    stack.append((row, col))
                    while stack:
                        curr_row, curr_col = stack.pop()
                        curr_area += 1
                        grid[curr_row][curr_col] = 0

                        for row_offset, col_offset in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            if curr_row + row_offset >= 0 and curr_row + row_offset < len(grid) and curr_col + col_offset >= 0 and curr_col + col_offset < len(grid[0]) and grid[curr_row + row_offset][curr_col + col_offset] == 1:
                                stack.append(
                                    (curr_row + row_offset, curr_col + col_offset))
                                grid[curr_row + row_offset][curr_col +
                                                            col_offset] = 0
                max_area = max(max_area, curr_area)

        return max_area
