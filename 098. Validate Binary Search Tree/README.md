# 98. Validate Binary Search Tree

## Solution 1

Use divide and conquer to iterate each node from the top to the bottom

* Time Complexity: O(N)
* Space Complexity: O(N), we call N times recursion

## Solution 2

The idea is same as solution1, but use DFS+stack to replace recursion.

* Time Complexity: O(N)
* Space Complexity: O(N)

## Solution 3 - Inorder Traversal (brillent!)

Based on the feature of binary search tree, if we run an inorder traversal, the visited numbers will form an ascending order.

* Time Complexity: O(N)
* Space Complexity: O(N)

