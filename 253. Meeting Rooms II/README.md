# 253. Meeting Rooms II
## Solution 1
Sort the intervals array based on each of start time of every interval. Then apply min heap for keeping the most closing end time. If the end time < the start time of the selected interval time, the two times are compatible. Otherwise, we need to open a new room for it, which means we put the time into the mim heap. Finally, the length of the min heap is the number of rooms we need.
* Time Complexity: O(NlogN)
* Space Complexity: O(N)

## Solution 2
Sort the intervals array based on each of start time of every interval. Then apply min heap for keeping the most closing end time. If the end time < the start time of the selected interval time, the two times are compatible. Otherwise, we need to open a new room for it, which means we put the time into the mim heap. Finally, the length of the min heap is the number of rooms we need.
* Time Complexity: O(NlogN)
* Space Complexity: O(1)