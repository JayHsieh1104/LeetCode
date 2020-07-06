from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # If string p is longer than string s, this means there is no answer.
        if len(p) > len(s):
            return []

        dict_s = defaultdict(int)
        dict_p = defaultdict(int)
        ret = []

        for i in range(len(p)):
            dict_p[p[i]] += 1
            dict_s[s[i]] += 1
        
        if dict_p == dict_s:
            ret.append(0)

        for i in range(len(s) - len(p)):
            # Add the next char into dict_s
            dict_s[s[i+len(p)]] += 1
            
            # Remove the current char from dict_s
            if dict_s[s[i]] > 1:
                dict_s[s[i]] -= 1
            else:
                del dict_s[s[i]]

            # If the new dict is same as the dict_p, this means the chars in substring S and string P are the same.
            if dict_s == dict_p:
                ret.append(i+1)
        
        return ret