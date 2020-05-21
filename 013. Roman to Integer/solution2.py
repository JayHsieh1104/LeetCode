class Solution:
    def romanToInt(self, s: str) -> int:
        mDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = mDict[s[-1]]
        i = 0
        for i in reversed(range(len(s)-1)):
            if mDict[s[i]] < mDict[s[i+1]]:
                sum -= mDict[s[i]]
            else:
                sum += mDict[s[i]]
        return sum