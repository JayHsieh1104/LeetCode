from collections import defaultdict
import queue

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or endWord not in wordList:
            return 0
        
        counter = 0
        wordList.append(beginWord)
        transformation = defaultdict(list)
        
        for word in wordList:
            for j in range(len(word)):
                transformation[word[:j] + "*" + word[j+1:]].append(word)

        q = queue.Queue()
        q.put(beginWord)
        usedWord = set()
        usedWord.add(beginWord)
        
        while not q.empty():
            counter += 1
            for _ in range(q.qsize()):
                currWord = q.get()
                if currWord == endWord:
                    return counter
                for i in range(len(currWord)):
                    if currWord[:i] + "*" + currWord[i+1:] not in usedWord:
                        for nextWord in transformation[currWord[:i] + "*" + currWord[i+1:]]:
                            if nextWord not in usedWord:
                                q.put(nextWord)
                                usedWord.add(nextWord)
        
        return 0