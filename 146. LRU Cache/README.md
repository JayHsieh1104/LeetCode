# 146. LRU Cache

## Solution 1 -- Ordered dictionary

Ordered dictionary, a data structure which combines behind both hashmap and linked list.

* Time Complexity: O(1)

* Space Complexity: O(N), N is the capacity of the cache

## Solution 2 -- Dictionary + Double Linked List

The idea of the solution is like No. 200, Number of Islands. Use BFS to rot the adjacent cells. If there is a fresh orange which can't be rotten. Then return -1

* Time Complexity: O(1)

* Space Complexity: O(N), N is the capacity of the cache