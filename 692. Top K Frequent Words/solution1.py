class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words)
        candicates = list(count.items())
        candicates.sort(key = lambda word: (-word[1], word[0]))
        return [item[0] for item in candicates[:k]]