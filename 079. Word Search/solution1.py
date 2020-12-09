class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def backtracking(row, col, remained_word):
            if remained_word == "":
                return True
            elif row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != remained_word[0]:
                return False
            else:
                board[row][col] = "#"
                for row_offset, col_offset in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if backtracking(row + row_offset, col + col_offset, remained_word[1:]):
                        return True
                board[row][col] = remained_word[0]

        for row in range(len(board)):
            for col in range(len(board[0])):
                if backtracking(row, col, word):
                    return True
        return False
