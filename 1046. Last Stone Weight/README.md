# 1046. Last Stone Weight

## Solution 1

Sort the input list first, then pop the last two heaviest stones and insert the weight of the new stone to the list.
When inserting a new stone, we use binary search to find where we should put it. However, the the operation for inserting an element into a sorted array takes O(N) time. Therefore, the total time is O(N^2)

* Time Complexity: O(N^2)
* Space Complexity: O(1)

## Solution 2

Convert the input list into a heap, which takes O(N) time. Then, when we need to pop two elements and push the new stone weight into the heap. The three operation takes three O(logN) time. Because the main loop iterates up to N-1 times, this means the total time complexity is O(NlogN).

* Time Complexity: O(NlogN)
* Space Complexity: O(1), if we directly convert the input lsit into a heap
