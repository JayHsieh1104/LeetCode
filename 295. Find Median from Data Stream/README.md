# 295. Find Median from Data Stream

## Solution 1 -- Sort

* Time Complexity: O(NlogN), N is the number of elements.

* Space Complexity: O(N)

## Solution 2 -- Insertion sorting

* Time Complexity: O(logN + N), binary search and shift the N numbers.

* Space Complexity: O(N)

## Solution 3 -- Two heap

Split the whole array into two heap. One max-heap contains the smaller half of the numbers. Another min-heap contains the bigger half of the numbers.

* Time Complexity: O(logN)

* Space Complexity: O(N)

## Solution 4 -- Balance tree

TODO:

* Time Complexity: O(logN)

* Space Complexity: O(N)