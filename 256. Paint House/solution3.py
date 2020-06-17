class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        
        for n in range(1, len(costs)):
            costs[n][0] += min(costs[n-1][1], costs[n-1][2])
            costs[n][1] += min(costs[n-1][0], costs[n-1][2])
            costs[n][2] += min(costs[n-1][0], costs[n-1][1])
        
        return min(costs[-1])