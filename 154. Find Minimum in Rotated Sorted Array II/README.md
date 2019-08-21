# 154. Find Minimum in Rotated Sorted Array II
## Solution 1
The concept is almost same as solution 1 of problem 153, just need to take care the situation `nums[mid] == nums[hi]`.
* Time Complexity: O(N), when all elements are the same.
* Space Complexity: O(1)

## Thinking:
1. In duplicated situation, we can't use `nums[mid] >= nums[0]` to determine whether at the left of rotated point or not.
2. Use `nums[mid] > nums[hi]` is helpful.
3. **Delete the duplicated elements when** `nums[mid] == nums[hi]`, and this causes time complexity from O(logN) to O(N)