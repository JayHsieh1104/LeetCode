class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_binary = [0] * 32
        y_binary = [0] * 32
        counter = 0
        
        for i in range(31, -1, -1):
            if x >= 2 ** i:
                x_binary[i] = 1
                x -= 2 ** i
            if y >= 2 ** i:
                y_binary[i] = 1
                y -= 2 ** i
            if x_binary[i] != y_binary[i]:
                counter += 1
        
        return counter