class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lo = 1
        hi = len(nums) - 1
        
        while lo < hi:
            counter = 0
            pivot = lo + (hi - lo) // 2
            for num in nums:
                if num <= pivot:
                    counter += 1
            if counter <= pivot:
                lo = pivot + 1
            else:
                hi = pivot
        return lo