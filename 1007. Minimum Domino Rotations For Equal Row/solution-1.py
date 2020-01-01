class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def check(x: int) -> int:
            rotation_a = rotation_b = 0
            for i in range(len(A)):
                if A[i] != x and B[i] != x:
                    return -1
                elif A[i] != x:
                    rotation_b += 1
                elif B[i] != x:
                    rotation_a += 1
            return min(rotation_a, rotation_b)
        
        rotation1 = check(A[0])
        rotation2 = check(B[0])
        
        if rotation1 == rotation2 == -1:
            return -1
        elif rotation1 == -1:
            return rotation2
        elif rotation2 == -1:
            return rotation1
        else:
            return min(rotation1, rotation2)