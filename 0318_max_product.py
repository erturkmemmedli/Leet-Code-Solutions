from collections import Counter

class Solution:
    def maxProduct(self, words) -> int:
        dic = {}
        for word in words:
            mark = 0
            for char in set(word):
                mark |= 1 << (ord(char) - ord('a'))
            dic[mark] = max(dic.get(mark, 0), len(word))
        return max([dic[x] * dic[y] for x in dic for y in dic if not x & y] or [0])
