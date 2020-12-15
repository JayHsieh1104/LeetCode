class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        res = 0
        for i in range(len(A)):
            prefix_sum = 0
            for j in range(i, len(A)):
                prefix_sum += A[j]
                if prefix_sum % K == 0:
                    res += 1
        return res