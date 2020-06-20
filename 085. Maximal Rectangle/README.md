# 085. Maximal Rectangle

## Solution 0 -- Brute Force

* Time Complexity: O((NM)^3), where N is the number of the rows and M is the number of the columns.

* Space Complexity: O(1)

## Solution 1 -- DP

* Time Complexity: O(N*M^2), where N is the number of the rows and M is the number of the columns.

* Space Complexity: O(NM)

## Solution 2 -- Ascending Stack

[Why append(0) to the end of the dp array?](https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28917/AC-Python-clean-solution-using-stack-76ms)

* Time Complexity: O(N*M), where N is the number of the rows and M is the number of the columns.

* Space Complexity: O(M)

## Solution 3 -- DP - Maximum Height at Each Point

TODO:

* Time Complexity: O(N*M), where N is the number of the rows and M is the number of the columns.

* Space Complexity: O(M)
