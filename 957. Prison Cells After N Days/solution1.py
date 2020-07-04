class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        def getNextDay(lastcells):
            temp = [0] * len(lastcells)
            for i in range(1, len(temp)-1):
                if (lastcells[i-1] == 1 and lastcells[i+1] == 1) or (lastcells[i-1] == 0 and lastcells[i+1] == 0):
                    temp[i] = 1
            return tuple(temp) 

        seen = dict()
        isRepeated = False
        
        while N > 0:
            if not isRepeated:
                key = tuple(cells)
                if key in seen:
                    N = N % (seen[key] - N)
                    isRepeated = True
                else:
                    seen[key] = N
            if N > 0:
                N -= 1
                cells = getNextDay(cells)
        
        return cells