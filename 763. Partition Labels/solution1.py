class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        positionTable = {}
        for i in range(len(S)):
            if S[i] not in positionTable:
                positionTable[S[i]] = [i, i]
            else:
                positionTable[S[i]][1] = i
        
        startEnd_array = []
        for key in positionTable.keys():
            startEnd_array.append((positionTable[key][0], positionTable[key][1]))
        startEnd_array.sort(key=lambda k: k[0])
        
        processed_startEnd_array = []
        for start, end in startEnd_array:
            if not processed_startEnd_array or processed_startEnd_array[-1][1] < start:
                processed_startEnd_array.append([start, end])
            else:
                if end > processed_startEnd_array[-1][1]:
                    processed_startEnd_array[-1][1] = end
        
        ret = []
        for start, end in processed_startEnd_array:
            ret.append(end-start+1)
        return ret