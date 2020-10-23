class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_list = []
        pointer1 = pointer2 = 0
        while pointer1 != len(nums1) or pointer2 != len(nums2):
            if pointer1 == len(nums1):
                merged_list.append(nums2[pointer2])
                pointer2 += 1
            elif pointer2 == len(nums2):
                merged_list.append(nums1[pointer1])
                pointer1 += 1
            else:
                if nums1[pointer1] > nums2[pointer2]:
                    merged_list.append(nums2[pointer2])
                    pointer2 += 1
                else:
                    merged_list.append(nums1[pointer1])
                    pointer1 += 1
        
        if len(merged_list) % 2 == 0:
            return (merged_list[len(merged_list)//2 - 1] + merged_list[len(merged_list)//2]) / 2
        else:
            return merged_list[len(merged_list)//2]