from collections import defaultdict

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        unClearNum = set()
        usedNum = defaultdict(int)

        for num in arr:
            if k - (num % k) not in unClearNum:
                usedNum[num % k] += 1
                unClearNum.add(num % k)
            else:
                if usedNum[k - (num % k)] == 1:
                    unClearNum.remove(k - (num % k))
                usedNum[k - (num % k)] -= 1
        
        if 0 in usedNum and usedNum[0] % 2 == 0:
            unClearNum.remove(0)
        
        if unClearNum:
            return False
        else:
            return True