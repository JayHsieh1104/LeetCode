class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one = two = three = 0
        for num in nums:
            two |= one & num
            one ^= num
            three = one & two
            one &= ~three
            two &= ~three
        return one