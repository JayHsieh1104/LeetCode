class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        used_letter = {}
        i = j = 0
        
        for j in range(len(s)):
            if s[j] in used_letter:
                i = max(i, used_letter[s[j]] + 1)
            used_letter[s[j]] = j
            max_length = max(max_length, j - i + 1)
         
        return max_length