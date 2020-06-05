import random

class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)

    def pickIndex(self) -> int:
        target = random.randint(1, self.prefix_sums[-1])
        
        lo = 0
        hi = len(self.prefix_sums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if self.prefix_sums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
            
        return lo

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()