class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def partion(nums: List[int], lo: int, hi: int) -> int:
            pivot = nums[hi]
            i = lo
            for j in range(lo, hi):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[hi] = nums[hi], nums[i]
            return i
            

        def quick_sort(nums: List[int], lo: int, hi: int) -> List[int]:
            if lo < hi:
                partion_point = partion(nums, lo, hi)
                quick_sort(nums, lo, partion_point-1)
                quick_sort(nums, partion_point+1, hi)
            return nums
            
        return quick_sort(nums, 0, len(nums)-1)