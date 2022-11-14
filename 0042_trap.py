class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        trappedRain = 0
        for i, h in enumerate(height):
            if not stack:
                stack.append([h, i])
                continue
            if h == stack[-1][0]:
                stack[-1][1] = i
            elif h < stack[-1][0]:
                stack.append([h, i])
            else:
                while len(stack) > 1 and h > stack[-1][0]:
                    if h >= stack[-2][0]:
                        trappedRain += (stack[-2][0] - stack[-1][0]) * (i - stack[-2][1] - 1)
                        stack.pop()
                    else:
                        trappedRain += (h - stack[-1][0]) * (i - stack[-2][1] - 1)
                        stack.pop()
                if h == stack[-1][0]:
                    stack[-1][1] = i
                elif h < stack[-1][0]:
                    stack.append([h, i])
                else:
                    stack[0] = [h, i]
        return trappedRain
