# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        dimension_row, dimension_col = binaryMatrix.dimensions()
        current_row, current_col = 0, dimension_col - 1
        
        while current_row < dimension_row and current_col >= 0:
            if binaryMatrix.get(current_row, current_col) == 1:
                current_col -= 1
            else:
                current_row += 1
        
        if current_col == dimension_col - 1:
            return -1
        else:
            return current_col + 1