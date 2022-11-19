class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = ""
        count = {}
        for i in s:
            if len(stack) == 0:
                stack += i
                count[i] = [1]
                continue
            if i not in count:
                count[i] = [1]
            elif stack[-1] == i:
                count[i][-1] += 1
            else:
                count[i].append(1)
            stack += i
            if count[i][-1] == k:
                count[i].pop()
                if count[i] == []:
                    del(count[i])
                stack = stack[:-k]
        return stack

# Alternative solution

class Solution1:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if not stack or stack[-1][0] != char:
                stack.append((char, 1))
            else:
                if stack[-1][0] == char:
                    if stack[-1][1] == k - 1:
                        stack = stack[:-k+1]
                    else:
                        stack.append((char, stack[-1][1] + 1))
        stack = [i[0] for i in stack]
        return "".join(stack)
