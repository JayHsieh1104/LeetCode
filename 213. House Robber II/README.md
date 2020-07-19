# 213. House Robber II

## Solution 1 -- DP

Because the list is a circle list, this means that we can choose the first and the last node at the same time. Thus, we can compare the maximum outcome of robbing list[1:n] and list[0:n-1].

* Time Complexity: O(N), N is the length of given list.

* Space Complexity: O(1)
