class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        
        prev_row = costs[0]
        
        for n in range(1, len(costs)):
            current_row = costs[n]
            current_row[0] += min(prev_row[1], prev_row[2])
            current_row[1] += min(prev_row[0], prev_row[2])
            current_row[2] += min(prev_row[0], prev_row[1])
            prev_row = current_row
        
        return min(prev_row)