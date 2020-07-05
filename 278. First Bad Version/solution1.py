"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = sorted([i for s in schedule for i in s], key=lambda x: x.start)
        ret, pre = [], intervals[0]
        
        for interval in intervals[1:]:
            if interval.start <= pre.end and interval.end > pre.end:
                pre.end = interval.end
            elif interval.start > pre.end:
                ret.append(Interval(pre.end, interval.start))
                pre = interval
        return ret