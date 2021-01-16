class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = collections.defaultdict(list)
        
        for str in strs:
            char_counter = [0] * 26
            for char in str:
                char_counter[ord(char) - ord('a')] += 1
            group[tuple(char_counter)].append(str)
        
        return group.values()