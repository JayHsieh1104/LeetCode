class Solution {
    public boolean search(int[] nums, int target) {
        int lo = 0, hi = nums.length - 1;
        
        // Return false if input empty array
        if(nums.length == 0) {
            return false;
        }
        // If the array is sorted, just do binarySearch
        else if(nums[lo] < nums[hi]) {
            return binarySearch(nums, target, lo, hi);
        }
        
        while(lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] == target) {
                return true;
            }
            if(nums[mid] > nums[hi]) {
                // The left part of mid is sorted, if(target < nums[mid]), do binary search
                if(target < nums[mid] && binarySearch(nums, target, lo, mid - 1)) {
                    return true;
                }
                // Otherwise, search the right part
                else {
                    lo = mid + 1;
                }
            }
            else if(nums[mid] < nums[hi]) {
                // The right part of mid is sorted, if(target > nums[mid]), do binary search
                if(target > nums[mid] && binarySearch(nums, target, mid + 1, hi)) {
                    return true;
                }
                // Otherwise, search the left part
                else {
                    hi = mid - 1;
                }
            }
            // Remove duplicate elements
            else {
                hi--;
            }
        }        
        return false;
    }

    private boolean binarySearch(int[] nums, int target, int lo, int hi) {
        while(lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if(nums[mid] == target) {
                return true;
            }
            else if(nums[mid] > target) {
                hi = mid - 1;
            }
            else {
                lo = mid + 1;
            }
        }
        return false;
    }
}