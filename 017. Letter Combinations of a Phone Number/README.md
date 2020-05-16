# 017. Letter Combinations of a Phone Number

## Solution 1

Use backtracking method to get all of the possible string.

* Time Complexity: O(3^N*4^M), N is the number of {2,3,4,5.6.8} in the phone string, M is the number of {7, 9} in the phone string

* Space Complexity: O(N), the max depth of the recursion tree.

## Solution 2 -- iterative version