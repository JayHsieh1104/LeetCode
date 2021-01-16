class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        for start_pos in range(len(s)):
            seen = set()
            curr_length = 0
            for i in range(start_pos, len(s)):
                if s[i] in seen:
                    break
                curr_length += 1
                seen.add(s[i])
            max_length = max(max_length, curr_length)
            
        return max_length