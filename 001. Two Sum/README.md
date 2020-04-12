# 001. Two Sum
## Solution 1 - Brute Force
Loop through each element x and find if there is another element which equals target - x.
* Time Complexity: O(N^2)
* Space Complexity: O(1)

## Solution 2 - Two-pass Hash Table
In the first iteration, add each element's value and index into the hash table. Then, in the second iteration we check if each element's complement exists in the table.
* Time Complexity: O(N)
* Space Complexity: O(N)

## Solution 3 - One-pass Hash Table
In an iteration, we check if current element's complement exists in the table. If it exists, return the element's index. Else, add the current element's value and index into the hash table. 
* Time Complexity: O(N)
* Space Complexity: O(N)