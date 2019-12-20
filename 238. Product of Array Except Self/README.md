# 238. Product of Array Except Self
## Solution 1
Build array L and R for recording the product of index i's left side and right 
* Time Complexity: O(N)
* Space Complexity: O(N)

## Solution 2
Build an array ANS for recording the product of index i's left side. Then use a variable R for record the product of right side. ans[i] = ans[i] * R 
* Time Complexity: O(N)
* Space Complexity: O(1)