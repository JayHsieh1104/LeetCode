class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = j = 0
        used_char = {}
        ret = 0
        while j < len(s):
            if s[j] in used_char and i <= used_char[s[j]]:
                i = used_char[s[j]] + 1
            used_char[s[j]] = j
            j += 1
            if j - i > ret:
                ret = j - i 
        return ret