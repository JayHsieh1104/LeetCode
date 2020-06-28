class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        def getSubString(currString, n, k):
            if n == 0:
                return currString
            if k <= 2**(n - 1):
                if currString[-1] == "a":
                    return getSubString(currString+"b", n-1, k)
                else:
                    return getSubString(currString+"a", n-1, k)
            else:
                if currString[-1] == "c":
                    return getSubString(currString+"b", n-1, k-2**(n - 1))
                else:
                    return getSubString(currString+"c", n-1, k-2**(n - 1))
        
        # Can not find the kth string because k is too large
        if 3 * 2 ** (n - 1) < k:
            return ""  
        elif k <= 1 * 2**(n - 1):
            return getSubString("a", n-1, k)
        elif k <= 2 * 2**(n - 1):
            return getSubString("b", n-1, k - 1 * 2**(n-1))
        else:
            return getSubString("c", n-1, k - 2 * 2**(n-1))