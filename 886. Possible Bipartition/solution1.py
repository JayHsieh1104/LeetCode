class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        p = [x for x in range(N+1)]
        rank = [0] * (N+1)
        graph = collections.defaultdict(list)
        
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            elif rank[x] > rank[y]:
                p[ry] = rx
            elif rank[x] < rank[y]:
                p[rx] = ry
            else:
                p[ry] = rx
                rank[rx] += 1
            return True
        
        for x, y in dislikes:
            graph[x].append(y)
            graph[y].append(x)
        
        for i in range(N+1):
            if i in graph:
                x = find(i)
                x_dislike_first = find(graph[i][0])
                if x == x_dislike_first:
                    return False
                for j in range(1, len(graph[i])):
                    x_dislike = find(graph[i][j])
                    if x == x_dislike:
                        return False
                    union(x_dislike, x_dislike_first)
            
        return True