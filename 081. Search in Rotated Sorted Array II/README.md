# 081. Search in Rotated Sorted Array II
## Solution 1
Compared to 033. Search in Rotated Sorted Array, there are duplicate elements in the array. So we need to care about the situation `nums[lo] (pivot) == nums[mid]`

So, we can remove the duplicate elements by operation like `if(nums[mid] == nums[lo]) lo++;`

And then take advantage of the feature that the array can be splited into a sorted array and an unsorted array. Then if the target is in the sorted array, just do binary search. Otherwise, split the other array. Keep doing this until find the target or left the loop.
* Time Complexity: O(N)
* Space Complexity: O(1)