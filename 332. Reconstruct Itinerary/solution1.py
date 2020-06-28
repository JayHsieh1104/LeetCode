from collections import defaultdict

class Solution:
    def backtracking(self, path):
        if len(path) == self.n:
            self.answer = path
            return True

        for v in self.itineraryTable[path[-1]]:
            if self.unUsedTicket[(path[-1], v)] > 0:
                self.unUsedTicket[(path[-1], v)] -= 1
                ret = self.backtracking(path + [v])
                if ret:
                    return True
                self.unUsedTicket[(path[-1], v)] += 1
        return False
    
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.n = len(tickets) + 1
        self.unUsedTicket = defaultdict(int)
        self.itineraryTable = defaultdict(list)
        self.answer = ""

        for u, v in tickets:
            self.itineraryTable[u].append(v)
            self.unUsedTicket[(u, v)] += 1
        
        for key in self.itineraryTable.keys():
            self.itineraryTable[key].sort()

        self.backtracking(["JFK"])
        return self.answer