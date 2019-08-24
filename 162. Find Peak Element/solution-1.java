class Solution {
    public int findPeakElement(int[] nums) {
        int[] winner = nums.length % 2 == 0 ? 
            new int[nums.length / 2] : new int[nums.length / 2 + 1]; 
        if(nums.length % 2 == 1) {
            winner[winner.length - 1] = nums.length - 1;
        }
        for(int i = 0; i < nums.length - 1; i = i + 2) {
            if(nums[i] >= nums[i + 1]) {
                winner[i / 2] = i;
            }
            else {
                winner[i / 2] = i + 1;
            }
        }
        
        while(winner.length > 1) {
            int tempPos = 0;
            int[] temp = winner.length % 2 == 0 ? 
                new int[winner.length / 2] : new int[winner.length / 2 + 1];
            if(winner.length % 2 == 1) {
                temp[temp.length - 1] = winner[winner.length - 1];
            }
            for(int i = 0; i < winner.length - 1; i = i + 2) {
                if(nums[winner[i]] >= nums[winner[i + 1]]) {
                    temp[tempPos] = winner[i];
                }
                else {
                    temp[tempPos] = winner[i + 1];
                }
                tempPos++;
            }
            winner = deepCopy(temp);
        }
        return winner[0];
    }
    
    private int[] deepCopy(int[] nums) {
        int[] temp = new int[nums.length];
        for(int i = 0; i < nums.length; i++) {
            temp[i] = nums[i];
        }
        return temp;
    }
}