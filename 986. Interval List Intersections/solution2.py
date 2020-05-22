class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        P1 = P2 = 0
        ret = []
        while P1 < len(A) and P2 < len(B):
            lo = max(A[P1][0], B[P2][0])
            hi = min(A[P1][1], B[P2][1])
            if lo <= hi:
                ret.append([lo, hi])
            if A[P1][1] <= B[P2][1]:
                P1 += 1
            else:
                P2 += 1
        return ret