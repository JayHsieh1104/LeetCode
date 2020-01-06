class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        R, C = len(matrix), len(matrix[0])
        seen = [[False] * C for _ in matrix]
        ans = []
        dc = [1, 0, -1, 0]
        dr = [0, 1, 0, -1]
        r = c = di = 0
        for _ in range(R * C):
            ans.append(matrix[r][c])
            seen[r][c] = True
            nextR, nextC = r + dr[di], c + dc[di]
            if 0 <= nextR < R and 0 <= nextC < C and not seen[nextR][nextC]:
                r = nextR
                c = nextC
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return ans