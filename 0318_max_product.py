class Solution:
    def maxProduct(self, words) -> int:
        dic = {}
        for word in words:
            mark = 0
            for char in set(word):
                mark |= 1 << (ord(char) - ord('a'))
            dic[mark] = max(dic.get(mark, 0), len(word))
        return max([dic[x] * dic[y] for x in dic for y in dic if not x & y] or [0])

# Alternative solution (which gives TLE error)

from collections import Counter

class Solution1:
    def maxProduct(self, words: List[str]) -> int:
        maximum = 0
        for i in range(0, len(words)):
            for j in range(i+1, len(words)):
                c1 = Counter(words[i])
                c2 = Counter(words[j])
                if c1 == c1 - c2:
                    maximum = max(maximum, len(words[i]) * len(words[j]))
        return maximum
