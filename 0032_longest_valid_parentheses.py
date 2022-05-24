class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = []
        stack = []
        for i, parantheses in enumerate(s):
            if parantheses == ')':
                if not stack:
                    dp.append(0)
                else:
                    stack.pop()
                    dp.append(2)
            else:
                stack.append(parantheses)
                dp.append(0)
        counter = 0
        index = len(dp) - 1
        for i in range(0, len(dp)):
            if dp[i] == 2:
                counter += 1
                index = min(index, i)
            else:
                c = 0
                while c < counter:
                    if dp[index - c] == 1 or dp[index - c] == 2:
                        index -= 1
                        continue
                    dp[index - c] = 1
                    c += 1
                counter = 0
                index = len(dp) - 1
            if i == len(dp) - 1:
                c = 0
                while c < counter:
                    if dp[index - c] == 1 or dp[index - c] == 2:
                        index -= 1
                        continue
                    dp[index - c] = 1
                    c += 1
        maximum = 0
        temp = 0
        for num in dp:
            if num == 0:
                temp = 0
            if num == 1:
                continue
            if num == 2:
                temp += 2
                maximum = max(maximum, temp)
        return maximum
