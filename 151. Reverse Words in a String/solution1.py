class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        ret = ""
        if len(s) > 0:
            for i in range(len(s) - 1, -1, -1):
                ret += " " + s[i]
        
        return ret[1:]