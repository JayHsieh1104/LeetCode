class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        
        intervals.sort(key=lambda item: item[0])
        
        output = [intervals[0]]
        for i in range(1, len(intervals)):
            if output[-1][1] < intervals[i][0]:
                output.append(intervals[i])
            elif output[-1][1] <= intervals[i][1]:
                output[-1][1] = intervals[i][1]              
        
        return output