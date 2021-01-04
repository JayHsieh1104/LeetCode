class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        while len(arr) > 1:
            min_num_pos = arr.index(min(arr))
            if 0 < min_num_pos < len(arr) - 1:
                res += arr[min_num_pos] * min(arr[min_num_pos - 1], arr[min_num_pos + 1])
            elif min_num_pos == 0:
                res += arr[min_num_pos] * arr[min_num_pos + 1]
            elif min_num_pos == len(arr) - 1:
                res += arr[min_num_pos] * arr[min_num_pos - 1]
            arr.pop(min_num_pos)
            
        return res