# 042. Trapping Rain Water

## Solution 0 -- Brute Force

* Time Complexity: O(N^2)

* Space Complexity: O(1)

## Solution 1

First, use DP to get the maximum wall heights from left to right. Second, use DP to get the minimum wall heights from right to left. Finally, calculate DP[i] - wall height[i] in range(len(wallHeight))

* Time Complexity: O(N)

* Space Complexity: O(N)

## Solution 2 -- Two pointers

Use four pointers to solve the problem. Two pointers are used for recording the current pointers on the right hand side and left hand side. The other two pointers are used for the highest wall on the left and the one on the right respectly. The volume for containing water on each position is the height of the position subtract the height of the min(leftWallHeight, rightWallHeight)

* Time Complexity: O(N)

* Space Complexity: O(1)

Last modified: 05/09, 2020