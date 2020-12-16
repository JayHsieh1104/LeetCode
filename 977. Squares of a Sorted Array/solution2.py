class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        N = len(nums)
        curr_pointer = 0
        while curr_pointer < N and nums[curr_pointer] < 0:
            curr_pointer += 1
        prev_pointer = curr_pointer - 1
        
        res = []
        while 0 <= prev_pointer and curr_pointer < N:
            if nums[prev_pointer]**2 > nums[curr_pointer]**2:
                res.append(nums[curr_pointer]**2)
                curr_pointer += 1
            else:
                res.append(nums[prev_pointer]**2)
                prev_pointer -= 1
                
        while 0 <= prev_pointer:
            res.append(nums[prev_pointer]**2)
            prev_pointer -= 1
            
        while curr_pointer < N:
            res.append(nums[curr_pointer]**2)
            curr_pointer += 1
                    
        return res