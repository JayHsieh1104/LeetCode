# 684. Redundant Connection

## Solution 1 -- DFS

Detect whether there would be a cycle in the graph if we add the current edge into the graphy. If it would, this means the edge is redundant.

* Time Complexity: O(N^2)

* Space Complexity: O(N)

## Solution 2 -- Union-Find

* Time Complexity: O(Nα(N)) ≈ O(N)
  * Find: O(logN)
  * Union: O(logN)

* Space Complexity: O(N)
