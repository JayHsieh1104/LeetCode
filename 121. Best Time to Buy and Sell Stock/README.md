# 121. Best Time to Buy and Sell Stock
## Solution 1
Use DP to solve the problem.
* Time Complexity: O(N)
* Space Complexity: O(N)

## Solution 2
Use DP to solve the problem. Because we only need to store the maximum profit, we can use only one variable to record it. We don't need to record all the list for all the profit at position i. Thus, the space complexity is O(1).
* Time Complexity: O(N)
* Space Complexity: O(1)