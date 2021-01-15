import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        hq = []
        for key, value in freq.items():
            if len(hq) < k:
                heapq.heappush(hq, (value, key))
            elif value > hq[0][0]:
                heapq.heappushpop(hq, (value, key))
        
        return [pair[1] for pair in hq]