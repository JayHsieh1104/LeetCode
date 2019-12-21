class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval[0], newInterval[1]
        index, n = 0, len(intervals)
        output = []

        while index < n and intervals[index][0] < new_start:
            output.append(intervals[index])
            index += 1
        
        if not output or output[-1][1] < newInterval[0]:
            output.append(newInterval)
        else:
            output[-1][1] = max(output[-1][1], newInterval[1])

        while index < n:
            if intervals[index][0] <= output[-1][1]:
                output[-1][1] =  max(output[-1][1], intervals[index][1])
            else:
                output.append(intervals[index])
            index += 1

        return output
