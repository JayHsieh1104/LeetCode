class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lo = 1
        hi = len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            counter = 0
            for i in range(len(nums)):
                if nums[i] <= mid:
                    counter += 1
            if counter > mid:
                hi = mid
            else:
                lo = mid + 1
        return lo