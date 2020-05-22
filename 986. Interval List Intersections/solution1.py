class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        P1 = P2 = 0
        ret = []
        while P1 != len(A) and P2 != len(B):
            if A[P1][1] <= B[P2][1]:
                if A[P1][0] >= B[P2][0]:
                    ret.append([A[P1][0], A[P1][1]])
                else:
                    if B[P2][0] <= A[P1][1]:
                        ret.append([B[P2][0], A[P1][1]])
                if P1 < len(A):
                    P1 += 1
            else:
                if B[P2][0] >= A[P1][0]:
                    ret.append([B[P2][0], B[P2][1]])
                else:
                    if A[P1][0] <= B[P2][1]:
                        ret.append([A[P1][0], B[P2][1]])
                if P2 < len(B):
                    P2 += 1
        return ret