# 009. Palindrome Number

## Solution 1 -- Two Pointers

* Time Complexity: O(N), where N is the length of given integer

* Space Complexity: O(1)

## Solution 2

Use a stack to contain each digit of the give integer, and then pop elements from the stack for rebuilding a interger. If the new built integer is same as the original integer, this means the original integer is palindrome.

* Time Complexity: O(N), where N is the length of given integer

* Space Complexity: O(N)
  
## Solution 3 -- Revert half of the number

* Time Complexity: O(N), where N is the length of given integer

* Space Complexity: O(1)
