class Solution {
    public int search(int[] nums, int target) {
        // Take care of empty array
        if(nums.length == 0) {
            return -1;
        }
        
        int pivot = nums[0];
        boolean flag = target >= pivot ? true : false;
        int lo = 0, hi = nums.length;
        
        if(flag) {
            while(lo <= hi) {
                int mid = lo + (hi - lo) / 2;
                // Out of boundary when not finding target
                if(mid >= nums.length) {
                    return -1;
                }
                else if(nums[mid] == target) {
                    return mid;
                }
                // In the same part, but target > mid
                else if(nums[mid] >= pivot && nums[mid] < target) {
                    lo = mid + 1;
                }
                // In the same part, but target < mid
                else if(nums[mid] >= pivot && nums[mid] > target) {
                    hi = mid - 1;
                }
                // In different part, just go left
                else {
                    hi = mid - 1;
                }
            }
            return -1;
        }
        else {
            while(lo <= hi) {
                int mid = lo + (hi - lo) / 2;
                // Out of boundary when not finding target
                if(mid >= nums.length) {
                    return -1;
                }
                if(nums[mid] == target) {
                    return mid;
                }
                // In the same part, but target < mid
                else if(nums[mid] < pivot && nums[mid] > target) {
                    hi = mid - 1;
                }
                // In the same part, but target > mid
                else if(nums[mid] < pivot && nums[mid] < target) {
                    lo = mid + 1;
                }
                // In different part, just go right
                else {
                    lo = mid + 1;
                }
            }
            return -1;            
        }
    }
}