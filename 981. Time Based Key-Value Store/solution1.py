class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mDict = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mDict[key].append((value, timestamp))
            

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mDict:
            return ""
        else:
            lo, hi = 0, len(self.mDict[key])
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if self.mDict[key][mid][1] <= timestamp:
                    lo = mid + 1
                else:
                    hi = mid
            if hi == 0:
                return ""
            else:
                return self.mDict[key][hi - 1][0]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)