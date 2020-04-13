class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) >= 2:
            s1 = stones.pop()
            s2 = stones.pop()
            if s1 == s2:
                continue
            
            lo = 0
            hi = len(stones)
            mid = 0
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if stones[mid] < s1 - s2:
                    lo = mid + 1
                else:
                    hi = mid
            stones.insert(lo, s1 - s2)
            
        return stones[0] if stones else 0