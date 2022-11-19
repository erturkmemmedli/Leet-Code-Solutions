class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {k:v for v, k in enumerate(order)}
        for i in range(1, len(words)):
            l = len(min(words[i], words[i-1], key = len))
            for j in range(l):
                if d[words[i][j]] > d[words[i-1][j]]:
                    break
                if d[words[i][j]] == d[words[i-1][j]]:
                    if j == l-1 and len(words[i-1]) > len(words[i]):
                        return False
                    continue
                if d[words[i][j]] < d[words[i-1][j]]:
                    return False
        return True
