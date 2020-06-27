class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        counter = 0
        for i in range(1, int(math.sqrt(n))+1):
            if n % i == 0:
                counter += 1
                if counter == k:
                    return i
                
        if 2 * counter < k:
            return -1
                
        for i in range(int(math.sqrt(n))+1, n+1):
            if n % i == 0:
                counter += 1
                if counter == k:
                    return i
        
        return -1