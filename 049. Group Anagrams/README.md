# 49. Group Anagrams

## Solution 1

Visit each string and count the chars in the string. Then, convert each counted result as a tuple object and store as a key in a dictionary. Finally, output the values of the dictionary.

* Time Complexity: O(NM), M = the average number of char in each string.

* Space Complexity: O(NM)