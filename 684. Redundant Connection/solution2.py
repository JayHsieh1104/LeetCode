class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [x for x in range(len(edges)+1)]
        rank = [0] * (len(edges)+1)
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            xr, yr = find(x), find(y)
            if xr == yr:
                return True
            elif rank[xr] < rank[yr]:
                parent[xr] = yr
            elif rank[xr] > rank[yr]:
                parent[yr] = xr
            else:
                parent[xr] = yr
                rank[xr] += 1
            return False
                
        for u, v in edges:
            if union(u, v):
                return [u, v]