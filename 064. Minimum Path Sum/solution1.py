from queue import Queue


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        mdict = {}
        q = Queue()
        q.put((0, 0, 0))

        while q.qsize() > 0:
            row, col, curr_sum = q.get()
            if (row, col) in mdict:
                mdict[(row, col)] = min(
                    mdict[(row, col)], curr_sum + grid[row][col])
            else:
                mdict[(row, col)] = curr_sum + grid[row][col]

            for row_offset, col_offset in ((0, 1), (1, 0)):
                if row + row_offset < len(grid) and col + col_offset < len(grid[0]):
                    q.put((row + row_offset, col + col_offset,
                           curr_sum + grid[row][col]))

        return mdict[(len(grid)-1, len(grid[0])-1)]
