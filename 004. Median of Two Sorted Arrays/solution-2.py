class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            m, n, nums1, nums2 = len(nums2), len(nums1), nums2, nums1
        else:
            m, n = len(nums1), len(nums2)
            
        i_min, i_max = 0, m
        while i_min <= i_max:
            i = int((i_min + i_max) / 2)
            j = int((m + n + 1) / 2) - i
            if i < m and j > 0 and nums1[i] < nums2[j-1]:
                i_min = i + 1
            elif i > 0 and j < n and nums1[i-1] > nums2[j]:
                i_max = i - 1
            else:
                if i == 0:
                    max_left = nums2[j-1]
                elif j == 0:
                    max_left = nums1[i-1]
                else:
                    max_left = max(nums1[i-1], nums2[j-1])
                
                if (m + n) % 2 == 1:
                    return max_left
                
                if i == m:
                    max_right = nums2[j]
                elif j == n:
                    max_right = nums1[i]
                else:
                    max_right = min(nums1[i], nums2[j])
                
                return (max_left + max_right) / 2
        