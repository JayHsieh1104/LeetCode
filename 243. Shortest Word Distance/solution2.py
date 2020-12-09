class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        index1 = -1
        index2 = -1
        min_distance = len(words)

        for i in range(len(words)):
            if words[i] == word1:
                index1 = i
            elif words[i] == word2:
                index2 = i

            if index1 != -1 and index2 != -1:
                min_distance = min(min_distance, abs(index1 - index2))
                
        return min_distance