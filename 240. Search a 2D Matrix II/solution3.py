class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        
        def search_rec(left, up, right, down):
            if left > right or up > down:
                return False
            elif target < matrix[up][left] or target > matrix[down][right]:
                return False
            
            col_mid = left + (right-left)//2
            
            row_mid = up
            while row_mid <= down and matrix[row_mid][col_mid] <= target:
                if matrix[row_mid][col_mid] == target:
                    return True
                row_mid += 1
                
            return search_rec(left, row_mid, col_mid-1, down) or search_rec(col_mid+1, up, right, row_mid-1)
    
        
        return search_rec(0, 0, len(matrix[0])-1, len(matrix)-1)