class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        
        // Take care of boundary testcase
        if(matrix.length == 0 || matrix[0].length == 0 || matrix == null) {
            return false;
        }
        
        // Get row, column value
        int rowNum = matrix.length;
        int colNum = matrix[0].length;
        
        // Calculate lo, hi value for binary search
        int lo = 0, hi = rowNum * colNum - 1;
        while(lo <= hi) {
            int mid = lo + (hi - lo) / 2; // Avoid mid value overflow
            // Find target
            if(matrix[mid / colNum][mid % colNum] == target) {
                return true;
            }
            // Search left side
            else if(matrix[mid / colNum][mid % colNum] > target) {
                hi = mid - 1;
            }
            // Search right side
            else {
                lo = mid + 1;
            }
        }
        // Not find the target
        return false;
    }
}