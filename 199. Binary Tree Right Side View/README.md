# 199. Binary Tree Right Side View

## Solution 1

We can apply revised DFS search to visit each node. The DFS search will firstly visit the right child, which is different from the regular DFS. We insert the node.val if the level is not visited before.

* Time Complexity: O(N)

* Space Complexity: O(N)

## Solution 2

We can apply BFS search to visit each node and then record the last node.val in each level.

* Time Complexity: O(N)

* Space Complexity: O(D), where D is the number of nodes at the widest level of the tree.
