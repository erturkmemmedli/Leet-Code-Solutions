class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = string.ascii_uppercase
        dictionary = {i+1:chr(65+i) for i in range(26)}
        l = []
        while columnNumber:
            l.append(columnNumber%26)
            columnNumber //= 26
        l = l[::-1]
        for i in range(len(l)-1,0,-1):
            if l[i] <= 0:
                l[i-1] -= 1
                l[i] += 26
        if l[0] == 0:
            l = l[1:]
        output = ""
        for i in l:
            output += dictionary[i]
        return output
