class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
     
        def merge(left_list: List[int], right_list: List[int]) -> List[int]:
            ret = []
            left_cursor = 0
            right_cursor = 0
            while left_cursor < len(left_list) and right_cursor < len(right_list):
                if left_list[left_cursor] < right_list[right_cursor]:
                    ret.append(left_list[left_cursor])
                    left_cursor += 1
                else:
                    ret.append(right_list[right_cursor])
                    right_cursor += 1
            ret.extend(left_list[left_cursor:])
            ret.extend(right_list[right_cursor:])
            return ret
        
        if len(nums) <= 1:
            return nums
            
        pivot = len(nums) // 2
        left_list = self.sortArray(nums[0:pivot])
        right_list = self.sortArray(nums[pivot:])
        return merge(left_list, right_list)     