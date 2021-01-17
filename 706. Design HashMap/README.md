# 706. Design HashMap

## Solution 1 -- Mode + Array

* Time Complexity:
  * Put: O(1)
  * Update: O(N/K), where N is the number of all possible keys and K is the number of buckets.
  * Delete: O(N/K)

* Space Complexity: O(K + M), where K is the number of predefined buckets in the hashmap and M is the number of unique keys that have been inserted into the hashmap.
