class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        for x in range(len(l)):
            temp = ''
            for i in range(len(l[x]) - 1, -1, -1):
                temp += l[x][i]
            l[x] = temp
        return ' '.join(l)
