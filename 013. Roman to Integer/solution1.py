class Solution:
    def romanToInt(self, s: str) -> int:
        mDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        i = 0
        while i < len(s):
            if i != len(s)-1 and mDict[s[i]] < mDict[s[i+1]]:
                sum += mDict[s[i+1]] - mDict[s[i]]
                i += 2
            else:
                sum += mDict[s[i]]
                i += 1
        return sum