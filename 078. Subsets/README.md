# 078. Subsets

## Solution 1

Use backtracking method to generate all of the possible subset.

- Time Complexity: O(N*2^N), The number of subsets is 2^N and each deep copy of subset takes O(N) time. So the total time complexity is O(N) * 2^N = O(N*2^N)

- Space Complexity: O(N*2^N)

## Solution 2 -- Cascading

- Time Complexity: O(N*2^N)

- Space Complexity: O(N*2^N)

## Solution 3 -- Bitmask

- Time Complexity: O(N*2^N)

- Space Complexity: O(N*2^N)
