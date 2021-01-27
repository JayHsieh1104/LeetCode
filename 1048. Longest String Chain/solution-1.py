class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        longest_length = 1
        
        for word in sorted(words, key=len):
            dp[word] = 1
            
            for i in range(len(word)):
                prev_word = word[:i] + word[i+1:]
                
                if prev_word in dp:
                    dp[word] = max(dp[prev_word] + 1, dp[word])
                    longest_length = max(dp[word], longest_length) 
        
        return longest_length