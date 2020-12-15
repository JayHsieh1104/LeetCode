class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        res = 0
        prefix_sum = 0
        prefix_sum_dict = collections.defaultdict(int)
        prefix_sum_dict[0] = 1
        for num in A:
            prefix_sum = (prefix_sum + (num % K) + K) % K
            res += prefix_sum_dict[prefix_sum]
            prefix_sum_dict[prefix_sum] += 1
        return res