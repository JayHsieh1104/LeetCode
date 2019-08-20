# 033. Search in Rotated Sorted Array
## Solution 1
Use nums[0] as a pivot to determine whether target and mid are in the same part 
* Time Complexity: O(logN)
* Space Complexity: O(1)

## Solution 2
Find the shifting value by finding the smallest value, and then calculate the original array
* Time Complexity: O(logN)
* Space Complexity: O(1)

## Solution 3
Take advantage the feature that there will be a sorted array when split the array to find target
* Time Complexity: O(logN)
* Space Complexity: O(1)
