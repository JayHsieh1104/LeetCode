import queue

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        ret = 0
        q = queue.Queue()
        
        for i in range(len(M)):
            if M[i][i] == 1:
                M[i][i] = 0
                ret += 1
            for j in range(i+1, len(M[0])):
                if M[i][j] == 1:
                    q.put(j)
                    M[i][j] = 0
                    M[j][i] = 0
            while q.qsize() > 0:
                next_num = q.get()
                M[next_num][next_num] = 0
                for j in range(0, len(M[0])):
                    if M[next_num][j] == 1:
                        q.put(j)
                        M[next_num][j] = 0
                        M[j][next_num] = 0
        
        return ret