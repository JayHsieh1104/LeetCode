# 019. Remove Nth Node From End of List
## Solution 1
Use two pointer to solve the problem. The first pointer advances the list by n+1 steps from the beginning, while the second pointer starts from the beginning. If the first pointer reachs the end of the list, remove the Nth node.
* Time Complexity: O(N)
* Space Complexity: O(1)