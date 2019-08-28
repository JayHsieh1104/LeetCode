# 023. Merge k Sorted Lists
## Solution 1. Brute Force Algorithm
1. Traverse all the linked lists and collect all the values of the nodes into an array.
2. Sort the array and then iterate over the array to get the value.
3. Build a linked list when iterating the array.
* Time Complexity: O(NlogN)
* Space Complexity: O(N)

## Solution 2
1. Compare each head of every linked list and then get the smallest value.
2. Add the selected node to the final linked list.
* Time Complexity: O(nk), k = the number of linked list in lists, n = the number of elements in the longest linked list.
* Space Complexity: O(1)

## Solution 3
1. Use priority queue to optimize the comparsion process in solution 2.
* Time Complexity: O(n logk), k = the number of linked list in lists, n = the number of elements in the longest linked list.
* Space Complexity: O(k), for creating heap

## Solution 4
1. Convert merge k lists problem to merge 2 lists (k-1) time
* Time Complexity: O(nk), k = the number of linked list in lists, n = the number of elements in the longest linked list.
* Space Complexity: O(1)

## Solution 5
1. Pick up k lists and merge each pair.
2. After the first pairing, k lists are merged into k/2 lists with average 2N/k length, then k/4, k/8 and so on.
3. Repeat the procedure until we get the final linked list.

* Time Complexity: O(n logk), k = the number of linked list in lists, n = the number of elements in the longest linked list.
* Space Complexity: O(1)