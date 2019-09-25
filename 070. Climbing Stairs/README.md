# 074. Search a 2D Matrix
## Solution 1
View the 2D matrix as a array and then just use binary search to search it.
* Time Complexity: O(logM+logN)
* Space Complexity: O(1)

### Pros:
1. Straightforward
2. Not need to care about boundary problem

### Cons:
1. `hi = rowNum * colNum - 1` may cause overflow for large rowNum and colNum
2. / and % are expensive operation

## Solution 2
Use binary search to search row first, and then search columns in the row.
* Time Complexity: O(logM+logN)
* Space Complexity: O(1)

### Pros:
1. Can be applied to large row and column, not lead to overflow
2. 

### Cons:
1. **Need to care about boundary problem**
2. 

## ToDo
Solution 2：注意二元搜尋到底後的停止位置？ 待解決
https://leetcode.com/problems/search-a-2d-matrix/discuss/26220/Don't-treat-it-as-a-2D-matrix-just-treat-it-as-a-sorted-list
			Ex. [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
				11