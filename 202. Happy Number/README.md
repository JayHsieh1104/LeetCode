# 202 Happy Number

## Solution 1

Use a while loop to let the process of calculating the happy number keep doing.
We are gonna use a set to detect if we've entered an cycle.
If we get the same number, this means we can't find the happy number because it's an infinite loop.

* Time Complexity: O(logN)
* Space Complexity: O(logN)

## Solution 2

View the question as detecting if a linkedlist has a cycle. Use Floyd's Cycle-Finding Algorithm (two pointers approach). If the two pointers meet at a same position, this means  the linkedlist has a cycle. Else, the faster pointer will arrive the final point, 1.

* Time Complexity: O(logN)
* Space Complexity: O(1), don't need a hashset to detect a cycle
