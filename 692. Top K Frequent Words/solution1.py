class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = collections.Counter(words)       
        candidates = list(freq.items())
        candidates.sort(key = lambda word: (-word[1], word[0]))
        
        return [key for key, value in candidates[:k]]