import sys

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        def DFS(n, last_color, current_sum):
            if n == len(costs):
                if current_sum < self.ret:
                    self.ret = current_sum
                return
            
            for i in range(3):
                if i == last_color:
                    continue
                DFS(n+1, i, current_sum+costs[n][i])
        
        if not costs:
            return 0
        
        self.ret = sys.maxsize
        
        for i in range(3):
            DFS(1, i, costs[0][i])
        
        return self.ret