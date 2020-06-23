import queue

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def isMutation(s1, s2):
            count = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    count += 1
                if count > 1:
                    return False
            return True
        
        if end not in bank:
            return -1
        
        bank.append(start)
        dist = [[False] * len(bank) for _ in range(len(bank))]
        for i in range(len(bank)):
            for j in range(len(bank)):
                if isMutation(bank[i], bank[j]):
                    dist[i][j] = True
        
        visited = set()
        q = queue.Queue()
        q.put(len(bank) - 1)

        mutation_step = -1
        while not q.empty():
            mutation_step += 1
            for t in range(q.qsize()):
                curr = q.get()
                if bank[curr] == end:
                    return mutation_step
                for j in range(len(bank) - 1):
                    if dist[curr][j] and j not in visited:
                        q.put(j)
                        visited.add(j)
                        
        return -1