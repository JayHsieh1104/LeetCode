class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = [0] * k

        for num in arr:
            freq[num % k] += 1
        
        for i in range(len(freq)):
            if i == 0:
                if freq[i] % 2 != 0:
                    return False
            elif freq[i] != freq[k-i]:
                return False
        return True