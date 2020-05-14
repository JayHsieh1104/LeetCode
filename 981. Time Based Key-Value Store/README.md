# 981. Time Based Key-Value Store

## Solution 1 -- Dictionary + Binary Search

* Time Complexity:
  * Get: O(logN)
  * Set: O(1)
  
* Space Complexity: O(N)

## Solution 2 -- TreeMap

The idea of the solution is like No. 200, Number of Islands. Use BFS to rot the adjacent cells. If there is a fresh orange which can't be rotten. Then return -1

* Time Complexity: O(N), N is the number of the toal grid cells

* Space Complexity: O(N)