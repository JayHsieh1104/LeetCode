import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        hq = []
        curMax = 0
        for i in range(len(nums)):
            hq.append((nums[i][0], i, 0))
            if nums[i][0] > curMax:
                curMax = nums[i][0]
        heapq.heapify(hq)

        _range = curMax - hq[0][0]
        start = hq[0][0]

        while True:
            cur_num = heapq.heappop(hq)
            # One of the lists is all visited, jump out of the while loop
            if cur_num[2]+1 == len(nums[cur_num[1]]):
                break
            next_num = (nums[cur_num[1]][cur_num[2]+1], cur_num[1], cur_num[2]+1)
            if next_num[0] > curMax:
                curMax = next_num[0]
            heapq.heappush(hq, next_num)
            if curMax - hq[0][0] < _range:
                start = hq[0][0]
                _range = curMax - start

        return [start, start+_range]