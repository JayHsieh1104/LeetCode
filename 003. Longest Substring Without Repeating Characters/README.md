# 003. Longest Substring Without Repeating Characters

## Solution 1 -- Brute Force

* Time Complexity: O(N^2)

* Space Complexity: O(1), using a set to record the visted letters among a-z.

## Solution 2 -- Sliding Window

* Time Complexity: O(N)

* Space Complexity: O(min(M, N)), where M is the size of the char set and N is the length of the longest substring.
