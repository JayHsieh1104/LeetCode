from collections import defaultdict
import bisect

class TimeMap:

    def __init__(self):
        self.mDict = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
            self.mDict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mDict:
            return ""
        else:
            lo = 0
            hi = len(self.mDict[key])
            
            while lo < hi:
                mid = int((lo + hi) / 2)
                if self.mDict[key][mid][0] <= timestamp:
                    lo = mid + 1
                else:
                    hi = mid
            
            if hi == 0:
                return ""
            else:
                return self.mDict[key][hi - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)