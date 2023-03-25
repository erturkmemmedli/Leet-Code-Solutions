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

# Alternative solution

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        output = [None] * n
        stack = []
        i = n - 1
        
        while i >= 0:
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()
                
            output[i] = 0 if not stack else stack[-1][1] - i
            stack.append((temperatures[i], i))
            i -= 1
            
        return output
