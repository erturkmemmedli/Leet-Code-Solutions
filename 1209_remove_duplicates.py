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
