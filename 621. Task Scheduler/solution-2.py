class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        
        f_max = max(freq)
        n_max = freq.count(f_max)
        
        return max(len(tasks), (f_max - 1) * (n + 1) + n_max)