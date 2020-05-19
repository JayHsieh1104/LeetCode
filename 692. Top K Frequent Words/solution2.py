import collections
import heapq

class Word:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
        
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        else:
            return self.freq < other.freq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words)
        freq = []
        heapq.heapify(freq)
        for key, value in count.items():
            heapq.heappush(freq, Word(key, value))
            if len(freq) > k:
                heapq.heappop(freq)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(freq).word)
        return res[::-1]