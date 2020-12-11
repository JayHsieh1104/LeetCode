class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        sorted_list = []
        seen = set()
        for num in nums:
            if num > 0 and num not in seen:
                sorted_list.append(num)
                seen.add(num)
        sorted_list.sort()
        for i in range(0, len(sorted_list)):
            if i+1 != sorted_list[i]:
                return i+1
        return len(sorted_list)+1