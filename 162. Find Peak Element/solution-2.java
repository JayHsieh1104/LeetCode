class Solution {
    public int findPeakElement(int[] nums) {
        int lo = 0, hi = nums.length - 1;
        while(lo < hi) {
            int mid = lo + (hi - lo) / 2;
            // If the function increases, search the right part of mid
            if(nums[mid] < nums[mid + 1]) {
                lo = mid + 1;
            }
            // Otherwise, search the left part of mid
            else {
                hi = mid;
            }
        }
        return lo;
    }
}