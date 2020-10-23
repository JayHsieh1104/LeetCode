# 015. 3Sum

## Solution 1

First, sort the nums array. Next, fix the first variable and use two pointers, one from the head of the rest of the array, another from the back of the rest of the array to estimate the sum of the three variables are zero or not.

- Time Complexity: O(N^2)

- Space Complexity: O(N), used for sorting

## Solution 2 -- Heshset

Fix one number and simplify the problem as a two sum problem.

- Time Complexity: O(N^2)

- Space Complexity: O(N), used for sorting

## Solution 3 -- Heshset (No-sort)

TODO:

- Time Complexity: O(N^2)

- Space Complexity: O(N)