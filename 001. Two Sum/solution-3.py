class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        for i in range(len(nums)):
            if nums[i] in hashTable:
                return [i, hashTable[nums[i]]]
            else:
                hashTable[target - nums[i]] = i