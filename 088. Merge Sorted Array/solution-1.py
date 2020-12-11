class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        current_pos = len(nums1) - 1
        while n > 0:
            if m == 0 or nums2[n-1] >= nums1[m-1]:
                nums1[current_pos] = nums2[n-1]
                n -= 1
            else:
                nums1[current_pos] = nums1[m-1]
                m -= 1
            current_pos -= 1
        