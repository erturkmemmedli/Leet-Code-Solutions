class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = [(temperatures[0], 0)]
        for i in range(1, len(temperatures)):
            if temperatures[i] <= stack[-1][0]:
                stack.append((temperatures[i], i))
            else:
                while stack and temperatures[i] > stack[-1][0]:
                    val, index = stack.pop()
                    answer[index] = i - index
                stack.append((temperatures[i], i))
        return answer
