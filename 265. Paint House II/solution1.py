class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        
        n = len(costs)
        k = len(costs[0])
        
        dp = [cost for cost in costs[0]]
        
        for i in range(1, n):
            temp = dp[:]
            
            fstMin = 0
            for j in range(1, k):
                if temp[j] < temp[fstMin]:
                    fstMin = j
                    
            if fstMin == 0:
                secMin = 1
            else:
                secMin = 0
            for j in range(k):
                if j == fstMin:
                    continue
                elif temp[j] < temp[secMin]:
                    secMin = j
                    
            for j in range(k):
                if j != fstMin:
                    dp[j] = costs[i][j] + temp[fstMin]
                else:
                    dp[j] = costs[i][j] + temp[secMin]
        
        return min(dp)