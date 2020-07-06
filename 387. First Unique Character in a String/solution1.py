class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = set()
        letter_frequency = {}

        for i in range(len(s)):
            if s[i] not in seen:
                seen.add(s[i])
                letter_frequency[s[i]] = i
            elif s[i] in letter_frequency:
                del letter_frequency[s[i]]
        
        if letter_frequency:
            for key in letter_frequency.keys():
                return letter_frequency[key]
        else:
            return -1