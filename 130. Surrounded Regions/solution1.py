class Solution:
    def solve(self, board: List[List[str]]) -> None:
         
        def DFS(x, y):
            if y < 0 or y >= len(board) or x < 0 or x >= len(board[0]) or board[y][x] != 'O':
                return
            else:
                board[y][x] = 'W'
                DFS(x+1, y)
                DFS(x-1, y)
                DFS(x, y+1)
                DFS(x, y-1)
            
        if not board:
            return board
        
        for y in [0, len(board)-1]:
            for x in range(0, len(board[0])):
                if board[y][x] == 'O':
                    DFS(x, y)
                    
        for y in range(0, len(board)):
            for x in [0, len(board[0])-1]:
                if board[y][x] == 'O':
                    DFS(x, y)
        
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == 'O':
                    board[y][x] = 'X'
                elif board[y][x] == 'W':
                    board[y][x] = 'O'