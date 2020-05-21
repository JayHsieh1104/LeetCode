import heapq

class MedianFinder:
    def __init__(self):
        self.hq1 = []
        self.hq2 = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.hq1, -1*num)
        heapq.heappush(self.hq2, -1*heapq.heappop(self.hq1))
        
        if len(self.hq1) < len(self.hq2):
            heapq.heappush(self.hq1, -1*heapq.heappop(self.hq2))

    def findMedian(self) -> float:
        if (len(self.hq1) + len(self.hq2)) % 2 == 1:
            return -1 * self.hq1[0]
        else:
            return (-1 * self.hq1[0] + self.hq2[0]) / 2