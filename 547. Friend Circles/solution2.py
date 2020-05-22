import queue

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        ret = 0
        seen = set()
        q = queue.Queue()
        
        for i in range(len(M)):
            if i not in seen:
                q.put(i)
                seen.add(i)
                ret += 1
                while q.qsize() > 0:
                    next_num = q.get()
                    for j in range(len(M[0])):
                        if j not in seen and M[next_num][j] == 1:
                            q.put(j)
                            seen.add(j)
            else:
                continue
        
        return ret