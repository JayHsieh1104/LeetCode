class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = temp = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        while True:
            temp = nums[temp]
            slow = nums[slow]
            if temp == slow:
                break
        return temp