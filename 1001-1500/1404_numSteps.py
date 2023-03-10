class Solution:
    def numSteps(self, s: str) -> int:
        s = list(s)
        step = 0
        while len(s) > 1:
            if s[-1] == '0':
                step += 1
                s.pop()
            else:
                temp = 1
                i = len(s) - 1
                while i >= 0:
                    if s[i] == '1':
                        temp += 1
                        i -= 1
                        s.pop()
                    else:
                        s[i] = '1'
                        step += temp
                        break
                if not s:
                    step += temp
                    break
        return step
