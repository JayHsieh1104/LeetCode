class Solution {
    public int[] twoSum(int[] nums, int target) {
        for(int i1 = 0; i1 < nums.length - 1; i1++) {
            for(int i2 = i1 + 1; i2 < nums.length; i2++) {
                if(target - nums[i1] == nums[i2]) {
                    return new int[] {i1, i2};
                }
            }
        }
        throw new IllegalArgumentException("No two sum solution");
    }
}