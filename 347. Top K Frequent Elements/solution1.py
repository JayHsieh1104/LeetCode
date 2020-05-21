from collections import defaultdict
import heapq

class Solution:
    def returnZero(self):
        return 0
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hq = []
        mDict = defaultdict(self.returnZero)
        mSet = set()
        for num in nums:
            mDict[num] += 1
            mSet.add(num)
        
        for num in mSet:
            if len(hq) < k:
                heapq.heappush(hq, (mDict[num], num))
            else:
                if mDict[num] > hq[0][0]:
                    heapq.heapreplace(hq, (mDict[num], num))
                    
        return [pair[1] for pair in hq]