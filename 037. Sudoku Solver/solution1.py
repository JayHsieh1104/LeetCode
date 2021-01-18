class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def findUnassigned():
            for row in range(9):
                for col in range(9):
                    if self.board[row][col] == ".":
                        return (row, col)
            return (-1, -1)
                
 
        def solve():
            row, col = findUnassigned()
            if (row, col) == (-1, -1):
                return True
            
            for num in map(str, range(1, 10)):
                if isSafe(row, col, num):
                    self.board[row][col] = num
                    if solve():
                        return True
                    self.board[row][col] = "."


        def isSafe(row: int, col: int, num: str) -> bool:
            rowSafe = all(self.board[row][_] != num for _ in range(9))
            colSafe = all(self.board[_][col] != num for _ in range(9))
            squareSafe = all(self.board[r][c] != num for r in getRange(row) for c in getRange(col))
            return rowSafe and colSafe and squareSafe
        
        
        def getRange(x):
            x -= x % 3
            return range(x, x + 3)
        
        
        self.board = board
        solve()