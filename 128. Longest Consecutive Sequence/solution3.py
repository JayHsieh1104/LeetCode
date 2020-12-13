class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_length = 0
        nums_set = set(nums)
        
        for num in nums:
            if num not in nums_set:
                continue
            else:
                prev_num = num - 1
                next_num = num + 1
                current_length = 1
                while prev_num in nums_set:
                    nums_set.remove(prev_num)
                    prev_num -= 1
                    current_length += 1
                while next_num in nums_set:
                    nums_set.remove(next_num)
                    next_num += 1
                    current_length += 1
                longest_length = max(longest_length, current_length)
        
        return longest_length