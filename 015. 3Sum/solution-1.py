class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        if len(nums) < 3:
            return output

        nums.sort()
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break

            if nums[i] == nums[i-1] and i > 0:
                continue

            target = -nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] == target:
                    output.append((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                    while j < k and nums[j-1] == nums[j]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    k -= 1

        return output