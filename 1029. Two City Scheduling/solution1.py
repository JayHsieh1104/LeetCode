class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: x[0] - x[1])
        
        minimim_cost = 0
        for i in range(0, len(costs)//2):
            minimim_cost += costs[i][0] + costs[len(costs)//2 + i][1]
            
        return minimim_cost