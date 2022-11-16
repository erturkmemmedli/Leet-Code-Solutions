class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if not stack:
                stack.append(asteroid)
                continue
            if asteroid > 0:
                stack.append(asteroid)
            elif stack[-1] < 0:
                stack.append(asteroid)
            else:
                while stack and stack[-1] > 0 and stack[-1] + asteroid < 0:
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(asteroid)
                elif stack[-1] + asteroid == 0:
                    stack.pop()
                elif stack[-1] + asteroid > 0:
                    continue
        return stack
