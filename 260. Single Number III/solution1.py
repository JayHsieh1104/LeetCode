class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        s = set()
        for num in nums:
            if num in s:
                s.remove(num)
            else:
                s.add(num)
        
        return [num for num in s]