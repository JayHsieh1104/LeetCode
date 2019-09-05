# 167. Two Sum II - Input array is sorted
## Solution 1 - Binary Search
Loop through each element x and find if its complement exists via binary search.
* Time Complexity: O(NlogN)
* Space Complexity: O(1)

## Solution 2 - Two pointers method
Initialize two pointers, the first pointer points to the first element. The second pointer points to the last element. If sum of the two pointers' value is great than target. Decrease the position of the second pointer by one. Else, Increase the position of first pointer by one. 
* Time Complexity: O(N)
* Space Complexity: O(1)