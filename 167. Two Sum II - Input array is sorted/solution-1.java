class Solution {
    public int[] twoSum(int[] numbers, int target) {
        for(int i = 0; i < numbers.length; i++) {
            int complement = target - numbers[i];
            int lo = i + 1, hi = numbers.length - 1;
            while(lo <= hi) {
                //System.out.println(lo + "   " + hi);
                int mid = lo + (hi - lo) / 2;
                if(numbers[mid] == complement) {
                    return new int[] {i + 1, mid + 1};
                }
                else if(numbers[mid] > complement) {
                    hi = mid - 1;
                }
                else {
                    lo = mid + 1;
                }
            }
        }
        throw new IllegalArgumentException("No two sum solution");
    }
}