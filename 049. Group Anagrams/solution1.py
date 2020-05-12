class Solution:
    def groupAnagrams(self, strs):
        ret = collections.defaultdict(list)
        
        for mStr in strs:
            alpha_set = [0] * 26
            for ch in mStr:
                alpha_set[ord(ch) - ord('a')] += 1
            ret[tuple(alpha_set)].append(mStr)
        return ret.values()