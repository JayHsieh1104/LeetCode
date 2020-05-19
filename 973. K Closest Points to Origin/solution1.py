import heapq

class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
        self.distance = _x**2 + _y**2
    
    def __lt__(self, other):
        return self.distance > other.distance

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        hq = []
        heapq.heapify(hq)
        for point in points:
            if len(hq) < K:
                heapq.heappush(hq, Point(point[0], point[1]))
            else:
                if point[0]**2 + point[1]**2 < hq[0].distance:
                    heapq.heappushpop(hq, Point(point[0], point[1]))
        ret = []
        for point in hq:
            ret.append([point.x, point.y])
        return ret