# 706. Design HashMap

## Solution 1 -- Mode + Array

* Time Complexity:
  * Put: O(1)
  * Update: O(K), need to find the key value pair in the bucket
  * Delete: O(K), need to find the key value pair in the bucket

* Space Complexity: O(N+K), N is the number of key value pair put in the hashmap. K the number of the hash collision occured.
