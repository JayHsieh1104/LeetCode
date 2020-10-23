class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) < 2:
            return intervals
        
        intervals.sort(key=lambda x: x[0])
        
        i = 1
        while i != len(intervals):
            if intervals[i][0] <= intervals[i - 1][1]:
                intervals[i - 1][1] = max(intervals[i - 1][1], intervals[i][1])
                del intervals[i]
            else:
                i += 1
        return intervals
            