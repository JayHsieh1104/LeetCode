from collections import Counter

class Solution:
    def reorganizeString(self, S: str) -> str:
        c = Counter(S)
        ret = ''
        
        if c.most_common(1)[0][1] > (len(S)+1) // 2:
            return ret

        while len(c) > 1:
            letter1, letter2 = c.most_common(2)
            ret += letter1[0] + letter2[0]
            if c[letter1[0]] != 1:
                c[letter1[0]] -= 1
            else:
                del c[letter1[0]]
            if c[letter2[0]] != 1:
                c[letter2[0]] -= 1
            else:
                del c[letter2[0]]
        
        if c:
            ret += c.most_common(1)[0][0]
        
        return ret