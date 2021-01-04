class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        self.cache = {}

        def helper(i, j):
            if (i, j) in self.cache:
                return self.cache[(i, j)]
            if i >= j:
                return 0

            res = float('inf')
            for k in range(i, j):
                rootVal = max(arr[i:k+1]) * max(arr[k+1:j+1])
                res = min(res, rootVal + helper(i, k) + helper(k + 1, j))

            self.cache[(i, j)] = res
            return res

        return helper(0, len(arr) - 1)
