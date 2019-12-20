# 289. Game of Life
## Solution 1
* Time Complexity: O(MN), M = the number of rows, N = the number of cols
* Space Complexity: O(MN), M = the number of rows, N = the number of cols

## Solution 2
For simultaneously updating each cell, we set cells which will be living in next round as 2, and cells which will be dead in the next round as -1. So we can update all cells without caring about the updating order
* Time Complexity: O(N)
* Space Complexity: O(1)

## Discussion
What would you do if the map is infinite?
https://leetcode.com/problems/game-of-life/discuss/73217/Infinite-board-solution/201780