class Solution {
    public int findMin(int[] nums) {
        int lo = 0, hi = nums.length - 1;
        
        // For not rotated sorted array or single number, just return nums[0]
        if(nums[0] <= nums[hi]) {
            return nums[0];
        }
        
        // Find the minimum number via binary search
        while(lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if(nums[mid] >= nums[0]) {
                lo = mid + 1;
            }
            else {
                hi = mid;
            }
        }
        return nums[lo];
    }
}