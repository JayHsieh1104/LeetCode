# 560. Subarray Sum Equals K

## Solution 0 -- Brute Force

Calculate all pairs [i, j]

- Time Complexity: O(N^3)

- Space Complexity: O(1)

## Solution 1 (TLE)

Calculate all pairs [i, j] with prefix sum

- Time Complexity: O(N^2), TLE, needed to be more efficient

- Space Complexity: O(N)

## Solution 2

Improved version of solution1. Only use constant time space

- Time Complexity: O(N^2)

- Space Complexity: O(1)

## Solution 3

For calculating all pairs [i, j], we can build a prefix sum array to do that. If P[j] - P[i] = k, this means P[i ~ j] = k.

But we can use one variable for calculating the current prefix sum, an array for all the prefix sums is not necessary.

Thus, we use a hash table to know whether P[i] = P[j] - k presents before the current prefix sum. If it does, we add hashtable[P[i]] to count. Finally, we add one to hashtable[current prefix sum]

- Time Complexity: O(N)

- Space Complexity: O(N)
