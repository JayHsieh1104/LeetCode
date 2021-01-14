class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {}
        for i in range(len(order)):
            order_dict[order[i]] = i
        
        for i in range(1, len(words)):
            word1 = words[i-1]
            word2 = words[i]
            
            for j in range(min((len(word1), len(word2)))):
                if word1[j] != word2[j]:
                    if order_dict[word1[j]] > order_dict[word2[j]]:
                        return False
                    else:
                        break
            
            if word1[:min((len(word1), len(word2)))] == word2[:min((len(word1), len(word2)))] and len(word1) > len(word2):
                return False
            
        return True