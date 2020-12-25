class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        result = 0
        
        seen = Counter(nums)
        
        for key, value in seen.items():
            if (k != 0 and key + k in seen) or (k == 0 and seen[key] > 1):
                result += 1
        
        return result
