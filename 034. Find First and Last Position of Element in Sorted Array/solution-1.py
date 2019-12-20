class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        begin, end = 0, len(nums)
        while begin <= end:
            mid = (begin + end) // 2
            if(nums[mid] < target):
                begin = mid + 1
            else:
                end = mid - 1
        start_point = mid

        while begin <= end:
            mid = (begin + end) // 2
            if(nums[mid] > target):
                end = mid - 1
            else:
                begin = mid + 1

        return List[start_point, mid]