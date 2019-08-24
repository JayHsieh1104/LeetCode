# 162. Find Peak Element
## Solution 1
I misunderstand the problem... So I just find the maximunm via comparing each element.
* Time Complexity: O(N/2)
* Space Complexity: O(N/2)

## Solution 2
Find a local minimum via binary search. In the end, the while loop will stop at a local minumum.
* Time Complexity: O(logN)
* Space Complexity: O(1)

## Thinking
### Why can we find the minimum value by binary search?