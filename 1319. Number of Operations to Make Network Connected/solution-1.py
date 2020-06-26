from collections import defaultdict

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        connectedTable = defaultdict(list)
        visited = [False] * n

        for u, v in connections:
            connectedTable[u].append(v)
            connectedTable[v].append(u)
        
        counter = 0
        for i in range(n):
            stack = []
            if not visited[i]:
                counter += 1
                stack.append(i)
            while stack:
                currentPoint = stack.pop()
                for connectedPoint in connectedTable[currentPoint]:
                    if not visited[connectedPoint]:
                        visited[connectedPoint] = True
                        stack.append(connectedPoint)
        return counter - 1