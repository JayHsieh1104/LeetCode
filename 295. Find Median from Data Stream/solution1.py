class MedianFinder:

    def __init__(self):
        self.array = []

    def addNum(self, num: int) -> None:
        self.array.append(num)

    def findMedian(self) -> float:
        self.array.sort()
        if len(self.array)%2 == 1:
            return self.array[len(self.array)//2]
        else:
            return (self.array[(len(self.array)//2)-1] + self.array[len(self.array)//2]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()