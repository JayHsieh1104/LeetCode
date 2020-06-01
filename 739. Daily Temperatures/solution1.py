class Solution:
    def getWarmerDay(self, index, T):
            for i in range(index+1, len(T)):
                if T[i] > T[index]:
                    return i - index
            return 0
    
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ret = []
        for i in range(len(T)):
            ret.append(self.getWarmerDay(i, T))
        
        return ret