# 240. Search a 2D Matrix II

## Solution 1 - Brute Force

Iterate each number to find if target is in the matrix

* Time Complexity: O(NM)
* Space Complexity: O(1)

## Solution 2 - Binary Search

If you find a sorted array, think about binary search!
Use binary search to do searching over the matrix diagonsals, eg. search the down and right line from matrix[0][0]
and then search the down and right line from matrix[1][1], and so on.

* Time Complexity: O(logN!), O(logN) + O(log N-1) + O(log N-2) +... O(log 1) = O(log N * N-1 * N-2 * ...) = O(logN!)
* Space Complexity: O(1)

## Solution 3 - Divide and conquer

Divide the matrix into 4 submatrixs, and then pick the two matrixs on right-top and left-down. Discard others.
Recursively do the above algorithm until we find the target or all of the submatrixs are visited. 

* Time Complexity: O(NlogN)
* Space Complexity: O(logN), logN layers of recursion

## Solution 4

Start from bottom-left or top-right corner to find the target number.

* Time Complexity: O(N+M)
* Space Complexity: O(1)