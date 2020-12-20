class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def next_status(is_living, row, col):
            live_neighbor = 0
            for row_offset, col_offset in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:
                if row + row_offset >= 0 and row + row_offset < len(board) and col + col_offset >= 0 and col + col_offset < len(board[0]):
                    if board[row + row_offset][col + col_offset] >= 1:
                        live_neighbor += 1

            if is_living:
                if live_neighbor < 2 or live_neighbor > 3:
                    return 2
                else:
                    return 1
            else:
                if live_neighbor == 3:
                    return -1
                else:
                    return 0

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 1:
                    board[row][col] = next_status(True, row, col)
                else:
                    board[row][col] = next_status(False, row, col)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 2:
                    board[row][col] = 0
                elif board[row][col] == -1:
                    board[row][col] = 1
