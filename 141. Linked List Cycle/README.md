# 141. Linked List Cycle
## Solution 1
Use hash table to record each visited nodes. If encounter an existed node when go through the linked list, that means the linked list contains cycle.
* Time Complexity: O(N)
* Space Complexity: O(N)

## Solution 2
Use one slower pointer and one faster pointer to solve the problem. Imagine two runners running on the same track at different speed.
* Time Complexity: O(N)
* Space Complexity: O(1)
