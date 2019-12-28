# 042. Trapping Rain Water
## Solution 0 -- Brute Force
* Time Complexity: O(N^2)
* Space Complexity: O(1)

## Solution 1
First, use DP to get the maximum wall heights from left to right. Second, use DP to get the minimum wall heights from right to left. Finally, calculate DP[i] - wall height[i] in range(len(wallHeight))
* Time Complexity: O(N)
* Space Complexity: O(N)

## Other solutions need to be understand...