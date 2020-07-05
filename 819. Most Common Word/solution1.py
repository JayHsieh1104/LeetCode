from collections import defaultdict

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned.append('')
        paragraph += ' '
        paragraph = paragraph.lower()
        anchor = 0
        word_frequency = defaultdict(int)
        for i in range(len(paragraph)):
            if paragraph[i] < 'a' or paragraph[i] > 'z':
                word_frequency[paragraph[anchor:i]] += 1
                for j in range(i + 1, len(paragraph)):
                    if 'a' <= paragraph[j] and paragraph[i] <= 'z':
                        anchor = j
                        break
        
        current_key = None
        max_frequency = 0
        for key in word_frequency.keys():
            if word_frequency[key] > max_frequency and key not in banned:
                current_key = key
                max_frequency = word_frequency[key] 
        
        return current_key