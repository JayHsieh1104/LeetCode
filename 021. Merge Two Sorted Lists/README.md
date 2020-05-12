# 021. Merge Two Sorted Lists

## Solution 1

Use two pointers to build the list iteratively.

* Time Complexity: O(N + M)

* Space Complexity: O(1)

## Solution 2 

Build the list recursively. The idea is that recursively go to the bottom of the list. Then build the new list from the bottom to top. 

* Time Complexity: O(N + M)

* Space Complexity: O(N + M)