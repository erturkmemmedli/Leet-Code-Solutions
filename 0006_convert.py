class Solution:
    def convert(self, s: str, row: int) -> str:
        if row == 1:
            return s
        i = 0
        reverse = False
        step = 0
        array = [[] for _ in range(row)]
        while i < len(s):
            if not reverse and step < row:
                array[step].append(s[i])
                i += 1
                step += 1
                continue
            if not reverse:
                step -= 1
            reverse = True
            if reverse and step > 0:
                array[step - 1].append(s[i])
                i += 1
                step -= 1
                continue
            if reverse:
                step += 1
            reverse = False
        result = ''
        for arr in array:
            result += ''.join(arr)
        return result