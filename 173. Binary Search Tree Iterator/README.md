# 173. Binary Search Tree Iterator

## Solution 1 -- Flattening the BST via inorder traversal

- Time Complexity:

  - Init: O(N), where N is the length of given binary search tree.
  - Next: O(1)
  - hasNext: O(1)

- Space Complexity: O(N)

## Solution 2 -- Brute Force

- Time Complexity:

  - Init: O(logN), where N is the length of given binary search tree.
  - Next: O(1), averagely
  - hasNext: O(1)

- Space Complexity: O(logN), averagely
