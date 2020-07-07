class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []
        for weight in asteroids:
            while stack and weight < 0 and stack[-1] > 0:
                if stack[-1] < -weight:
                    stack.pop()
                    continue
                elif stack[-1] == -weight:
                    stack.pop()
                break
            else:
                stack.append(weight)
        return stack