class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = j = 0
        while j < len(pushed):
            if not stack:
                stack.append(pushed[i])
                i += 1
            else:
                if i < len(pushed) and popped[j] != stack[-1]:
                    stack.append(pushed[i])
                    i += 1
                elif popped[j] == stack[-1]:
                    stack.pop()
                    j += 1
                else:
                    break
        return not stack
