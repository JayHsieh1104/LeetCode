class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1]
        l2 = l3 = l5 = 0
        while len(res) < n:
            m2 = res[l2] * 2
            m3 = res[l3] * 3
            m5 = res[l5] * 5
            next_ugly_num = min(m2, m3, m5)
            if next_ugly_num == m2:
                l2 += 1
            if next_ugly_num == m3:
                l3 += 1
            if next_ugly_num == m5:
                l5 += 1
            res.append(next_ugly_num)
        return res[-1]