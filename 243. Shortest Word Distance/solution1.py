class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        word1_pos = []
        word2_pos = []
        
        for i in range(len(words)):
            if words[i] == word1:
                word1_pos.append(i)
            elif words[i] == word2:
                word2_pos.append(i)
        
        min_distance = len(words)
        
        for i in range(len(word1_pos)):
            for j in range(len(word2_pos)):
                if abs(word1_pos[i] - word2_pos[j]) < min_distance:
                    min_distance = abs(word1_pos[i] - word2_pos[j])
        
        return min_distance