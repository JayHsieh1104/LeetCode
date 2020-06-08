class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for x, y in dislikes:
            graph[x].append(y)
            graph[y].append(x)
        
        color = {}
        def checkColor(node, c = 0):
            if node in color:
                return color[node] == c
            color[node] = c
            return all(checkColor(nei, not c) for nei in graph[node])
        
        return all(checkColor(node) for node in range(1, N+1) if node not in color)