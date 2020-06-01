class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = j = 0
        used_char = set()
        ret = 0
        while j < len(s):
            if s[j] not in used_char:
                used_char.add(s[j])
                j += 1
                if j - i > ret:
                    ret = j - i
            else:
                used_char.remove(s[i])
                i += 1
        
        return ret