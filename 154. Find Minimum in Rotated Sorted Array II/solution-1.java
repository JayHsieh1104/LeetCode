class Solution {
    public int findMin(int[] nums) {
        int lo = 0, hi = nums.length - 1;
        
        // For not rotated sorted array, just return nums[0]
        if(nums[0] < nums[hi]) {
            return nums[0];
        }
        
        // Find the minimum number via binary search
        while(lo < hi) {
            int mid = lo + (hi - lo) / 2;
            // Happen ar the left of rotated point => search the right part
            if(nums[mid] > nums[hi]) {
                lo = mid + 1;
            }
            // Happen at the right of rotated point => search the left part
            else if(nums[mid] < nums[hi]) {
                hi = mid;
            }
            // nums[mid] == nums[hi] => delete hi
            else {
                hi--;
            }
        }
        return nums[lo];
    }
}