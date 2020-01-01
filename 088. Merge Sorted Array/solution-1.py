class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for cur in range(len(nums1) - 1, -1, -1):
            if n == 0:
                break
            elif m == 0 or nums2[n - 1] >= nums1[m - 1]:
                nums1[cur] = nums2[n - 1]
                n -= 1
            else:
                nums1[cur] = nums1[m - 1]
                m -= 1