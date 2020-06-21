class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ret = ''
        used = set()
        permutation = [1] * (n + 1)
        for i in range(1, n+1):
            permutation[i] = permutation[i-1] * i
        k -= 1
        
        for i in range(n-1, -1, -1):
            number_order = 0
            for j in range(1, n+1):
                if j in used:
                    continue
                if number_order == k // permutation[i]:
                    ret += str(j)
                    used.add(j)
                    break
                number_order += 1
            k -= permutation[i] * (k // permutation[i])
            
        return ret