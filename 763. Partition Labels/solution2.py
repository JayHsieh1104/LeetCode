class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        lastSeenPos = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ret = []
        for i, c in enumerate(S):
            if lastSeenPos[c] > j:
                j = lastSeenPos[c]
            if i == j:
                ret.append(j - anchor + 1)
                anchor = j + 1
        
        return ret