# 1048. Longest String Chain
## Solution 1
Apply DP method to solve the problem. We start to split each string in the string list from the back of the list. 
* Time Complexity: O(NlogN + N x len(W') x len(W'')), N = the number of strings in the list, W' = the length of string, W'' = the substring generation
* Space Complexity: O(NS)

