class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 += nums2
        nums1.sort()
        lo = 0
        hi = len(nums1) - 1
        
        if hi % 2 == 0:
            return nums1[int((lo+hi)/2)]
        else:
            return (nums1[int((lo+hi)/2)] + nums1[int((lo+hi)/2) + 1])/2