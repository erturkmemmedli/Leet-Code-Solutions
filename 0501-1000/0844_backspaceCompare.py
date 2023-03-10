class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = 0
        while i < len(s) - 1:
            if s[0] == '#':
                s = s[1:]
                continue
            if s[i+1] == '#':
                s = s[:i] + s[i+2:]
                i -= 1
            else:
                i += 1
        j = 0
        while j < len(t) - 1:
            if t[0] == '#':
                t = t[1:]
                continue
            if t[j+1] == '#':
                t = t[:j] + t[j+2:]
                j -= 1
            else:
                j += 1
        return s == t
		
# Alternative solution

class Solution1:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        for i in range(len(s)):
            if s[i] != '#':
                stack1.append(s[i])
            elif stack1:
                stack1.pop()
        string1 = ''.join(stack1)
        stack2 = []
        for j in range(len(t)):
            if t[j] != '#':
                stack2.append(t[j])
            elif stack2:
                stack2.pop()
        string2 = ''.join(stack2)
        return string1 == string2

# Alternative solution

class Solution2:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = self.stack(s)
        stack_t = self.stack(t)
        return stack_s == stack_t

    def stack(self, sting):
        stack = []
        for char in sting:
            if char != "#":
                stack.append(char)
            elif stack:
                stack.pop()
        return stack
