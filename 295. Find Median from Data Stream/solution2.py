class MedianFinder:
    def __init__(self):
        self.array = []

    def addNum(self, num: int) -> None:
        lo = 0
        hi = len(self.array)
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if num > self.array[mid]:
                lo = mid + 1
            else:
                hi = mid
        
        self.array.insert(lo, num)

    def findMedian(self) -> float:
        if len(self.array)%2 == 1:
            return self.array[len(self.array)//2]
        else:
            return (self.array[(len(self.array)//2)-1] + self.array[len(self.array)//2]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()