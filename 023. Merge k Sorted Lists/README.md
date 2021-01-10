# 023. Merge k Sorted Lists

## Solution 1 -- Brute Force

* Time Complexity: O(NlogN), N is the number of total nodes.

* Space Complexity: O(N)

## Solution 2 -- Compare one by one

* Time Complexity: O(KN), K = the number of linkedlists, N = the number of nodes in the longest linkedlist.

* Space Complexity: O(1)

## Solution 3 -- Optimize Approach 2 by Priority Queue

* Time Complexity: O(NlogK), K = the number of linkedlists, N = the number of node in the longest linkedlist.

* Space Complexity: O(K), for creating the priority queue

## Solution 4 -- Merge lists one by one

* Time Complexity: O(KN), K = the number of linkedlists, N = the number of nodes in the longest linkedlist.

* Space Complexity: O(1)

## Solution 5 -- Merge with Divide And Conquer

TODO:

* Time Complexity: O(NlogK), K = the number of linked list in lists, N = the number of elements in the longest linked list.

* Space Complexity: O(1)
