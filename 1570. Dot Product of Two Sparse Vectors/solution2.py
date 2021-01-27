class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = []
        for index, value in enumerate(nums):
            if value != 0:
                self.nums.append((index, value))
        
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        sum = 0
        p1 = p2 = 0
        
        while p1 < len(self.nums) and p2 < len(vec.nums):
            if self.nums[p1][0] == vec.nums[p2][0]:
                sum += self.nums[p1][1] * vec.nums[p2][1]
                p1 += 1
                p2 += 1
            elif self.nums[p1][0] < vec.nums[p2][0]:
                p1 += 1
            else:
                p2 += 1
            
        return sum

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)