# 994. Rotting Oranges

## Solution 1 -- In-place BFS

Run in-place BFS traversal.

* Time Complexity: O(N^2), N is the number of the toal grid cells

* Space Complexity: O(1)

## Solution 2 -- BFS

The idea of the solution is like No. 200, Number of Islands. Use BFS to rot the adjacent cells. If there is a fresh orange which can't be rotten. Then return -1

* Time Complexity: O(N), N is the number of the toal grid cells

* Space Complexity: O(N)