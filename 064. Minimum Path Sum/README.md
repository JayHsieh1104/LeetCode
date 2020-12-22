# 064. Minimum Path Sum

## Solution 1

View the 2D matrix as a array and then just use binary search to search it.

* Time Complexity: O(logM+logN)

* Space Complexity: O(1)

# 064. Minimum Path Sum

## Solution 1 --- BFS (TLE)

* Time Complexity: O(MN), where M is the length of the rows and N is the length of the cols

* Space Complexity: O(MN)

## Solution 2 --- Top-Down DP

* Time Complexity: O(MN), where M is the length of the rows and N is the length of the cols

* Space Complexity: O(MN)

## Solution 3 --- Top-Down DP

The solution is simplified from solution 2, only using one row to maintain the dp array.

* Time Complexity: O(MN), where M is the length of the rows and N is the length of the cols

* Space Complexity: O(N)

## Solution 4 --- Top-Down DP

Directly modify the input array.

* Time Complexity: O(MN), where M is the length of the rows and N is the length of the cols

* Space Complexity: O(1)
