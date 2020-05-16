class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def backtracking(row, col, suffix):
            if len(suffix) == 0:
                return True
            
            if row < 0 or row == len(board) or col < 0 or col == len(board[0]) or \
            board[row][col] != suffix[0]:
                return False
            
            ret = False
            board[row][col] = '#'
            for row_offset, col_offset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ret = backtracking(row+row_offset, col+col_offset, suffix[1:])
                if ret:
                    break
                
            board[row][col] = suffix[0]
            
            return ret
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                    if backtracking(row, col, word):
                        return True
        return False