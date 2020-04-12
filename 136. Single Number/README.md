# 136 Single Number

## Solution 1

Iterate each element and record each number in a set.
When encounter an number, if it's not in the set, we push it into the set, or we remove it from the set.
The last number in the set is our answer.

* Time Complexity: O(N)
* Space Complexity: O(N)

## Solution 2

Use bit (XOR) operation to find the single number.

* Time Complexity: O(N)
* Space Complexity: O(1)
