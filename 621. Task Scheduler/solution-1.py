class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        
        freq.sort()
        
        f_max = freq.pop()
        idle_time = (f_max - 1) * n
        
        while freq and idle_time > 0:
            idle_time -= min(f_max - 1, freq.pop())
        
        idle_time = max(0, idle_time)
        
        return len(tasks) + idle_time