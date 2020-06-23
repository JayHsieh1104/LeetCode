class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        
        n = len(costs)
        k = len(costs[0])
        
        for i in range(1, n):
            fstMin = secMin = None
            for color in range(k):
                cost = costs[i-1][color]
                if fstMin is None or cost < costs[i-1][fstMin]:
                    secMin = fstMin
                    fstMin = color
                elif secMin is None or cost < costs[i-1][secMin]:
                    secMin = color
                    
            for color in range(k):
                if color != fstMin:
                    costs[i][color] += costs[i-1][fstMin]
                else:
                    costs[i][color] += costs[i-1][secMin]
        
        return min(costs[-1])