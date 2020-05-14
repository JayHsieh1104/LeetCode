class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_weight = {c: i for i, c in enumerate(order)}
        
        for i in range(len(words)-1):
            if len(words[i]) > len(words[i+1]) and words[i][:len(words[i+1])] == words[i+1]:
                return False
            else:   
                for j in range(len(words[i])):
                    if char_weight[words[i][j]] < char_weight[words[i+1][j]]:
                        break
                    elif char_weight[words[i][j]] == char_weight[words[i+1][j]]:
                        continue
                    elif char_weight[words[i][j]] > char_weight[words[i+1][j]]:
                        return False
                
        return True