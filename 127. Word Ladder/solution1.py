from collections import defaultdict
import queue

class Solution:
    def isTransformed(self, word1, word2):
        counter = 0
        for j in range(len(word1)):
            if word1[j] != word2[j]:
                counter += 1
                if counter > 1:
                    return False
        return True

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        n = len(wordList)
        transformation = defaultdict(list)
        
        for i in range(n):
            for j in range(n):
                if self.isTransformed(wordList[i], wordList[j]):
                    transformation[wordList[i]].append(wordList[j])

        q = queue.Queue()
        q.put(beginWord)
        usedWord = set()
        usedWord.add(beginWord)
        counter = 1
        while not q.empty():
            for _ in range(q.qsize()):
                currWord = q.get()
                if currWord == endWord:
                    return counter
                for nextWord in transformation[currWord]:
                    if nextWord not in usedWord:
                        q.put(nextWord)
                        usedWord.add(nextWord)
            counter += 1
        
        return 0