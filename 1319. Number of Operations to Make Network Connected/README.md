# 1319. Number of Operations to Make Network Connected

## Solution 1 DFS

* Time Complexity: O(N + K), where N is the total number of computers and K is the length of the connection list.
  * Build connectedTable: O(K)
  * Calculate isolated computer cluster: O(N)

* Space Complexity: O(N)
  * ConnectedTable: O(2K), as the description mentions, K is less than N.
  * Visited List: O(N)

## Solution 2 Union-Find

TODO:

* Time Complexity: O(N + K), where N is the total number of computers and K is the length of the connection list.
  * Build connectedTable: O(K)
  * Calculate isolated computer cluster: O(N)

* Space Complexity: O(N)
  * ConnectedTable: O(2K), as the description mentions, K is less than N.
  * Visited List: O(N)