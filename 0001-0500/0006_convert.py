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
    
# Alternative solution

class Solution1:
    def convert(self, s: str, numRows: int) -> str:
        zigzag = [[] for _ in range(numRows)]
        i = 0
        j = 0
        while i < len(s):
            while j < i + numRows and j < len(s):
                zigzag[j - i].append(s[j])
                j += 1
            while j < i + 2 * numRows - 2 and j < len(s):
                zigzag[numRows - j + i - 2].append(s[j])
                j += 1
            i = j
        answer = ""
        for l in zigzag:
            answer += "".join(l)
        return answer
