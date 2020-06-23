class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashMap = collections.Counter(nums)
        
        for num in hashMap.keys():
            if hashMap[num] == 1:
                return num