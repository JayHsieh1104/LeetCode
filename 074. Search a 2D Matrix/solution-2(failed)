class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if(matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return false;
        }
        
        if(matrix.length == 1) {
            return searchCol(matrix, target, 0);
        }
        else{
            int row = searchRow(matrix, target);
            if(row == -9) {
                return true;
            }
            return searchCol(matrix, target, row);
        }
    }
    
    private int searchRow(int[][] matrix, int target) {
        int lo = 0, hi = matrix.length - 1, mid = 0;
        while(lo <= hi) {
            mid = lo + (hi - lo) / 2;
            //System.out.println(mid + " " + lo + " " + hi);
            if(matrix[mid][0] == target) {
                return -9;
            }
            else if(matrix[mid][0] > target) {
                hi = mid - 1;
            }
            else {
                lo = mid + 1;
            }
        }
        return mid;
    }

    private boolean searchCol(int[][] matrix, int target, int row) {
        int lo = 0, hi = matrix[row].length - 1;
        while(lo <= hi) {
            //int mid = lo + (hi - lo) / 2;
            int mid = (lo + hi) / 2;
            if(matrix[row][mid] == target) {
                return true;
            }
            if(matrix[row][mid] > target) {
                hi = mid - 1;
            }
            else {
                lo = mid + 1;
            }
        }
        return false;
    }
}