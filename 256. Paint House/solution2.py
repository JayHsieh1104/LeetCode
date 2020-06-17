class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        def paint(n, last_color):
            if (n, last_color) in self.memo:
                return self.memo[(n, last_color)]
            elif n == len(costs) - 1:
                return costs[n][last_color]
            
            total_cost = costs[n][last_color]
            if last_color == 0:
                total_cost += min(paint(n+1, 1), paint(n+1, 2))
            elif last_color == 1:
                total_cost += min(paint(n+1, 0), paint(n+1, 2))
            elif last_color == 2:
                total_cost += min(paint(n+1, 0), paint(n+1, 1))
            self.memo[(n, last_color)] = total_cost
            return total_cost

        if not costs:
            return 0

        self.memo = {}
        return min(paint(0, 0), paint(0, 1), paint(0, 2))