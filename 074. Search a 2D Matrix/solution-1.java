class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        
        if(matrix.length == 0 || matrix[0].length == 0 || matrix == null) {
            return false;
        }
        
        int rowNum = matrix.length;
        int colNum = matrix[0].length;
        
        int lo = 0, hi = rowNum * colNum - 1;
        while(lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if(matrix[mid / colNum][mid % colNum] == target) {
                return true;
            }
            else if(matrix[mid / colNum][mid % colNum] > target) {
                hi = mid - 1;
            }
            else {
                lo = mid + 1;
            }
        }
        return false;
    }
}