class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        running_sum = 0
        hash_table = collections.defaultdict(lambda:0)
        hash_table[0] = 1
        for n in nums:
            running_sum += n
            if (running_sum - k) in hash_table:
                count += hash_table[running_sum - k]
            hash_table[running_sum] += 1
        return count