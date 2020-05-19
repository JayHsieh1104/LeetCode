class Solution(object):
    def kClosest(self, points, K):
        points.sort(key = lambda point: point[0]**2 + point[1]**2)
        return points[:K]