class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        m = collections.defaultdict(int)
        v = []
        ret = []
        
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                v.append((nums[i][j], i))
        v = sorted(v, key = lambda pair: pair[0])
        
        left = 0
        count = 0
        diff = float('inf')
        for right in range(len(v)):
            m[v[right][1]] += 1
            if m[v[right][1]] == 1:
                count += 1
            while count == len(nums) and left <= right:
                if v[right][0] - v[left][0] < diff:
                    diff = v[right][0] - v[left][0]
                    ret = [v[left][0], v[right][0]]
                m[v[left][1]] -= 1
                if m[v[left][1]] == 0:
                    count -= 1
                left += 1

        return ret