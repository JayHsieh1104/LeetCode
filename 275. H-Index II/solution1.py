class Solution:
    def hIndex(self, citations: List[int]) -> int:
        ret = 0
        while len(citations) - 1 - ret >= 0 and citations[len(citations) - 1 - ret] > ret:
            ret += 1
        
        return ret