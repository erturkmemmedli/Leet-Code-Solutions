from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        c = Counter(word).most_common()
        total = 0
        mult = 1
        cnt = 8
        i = 0

        while i < len(c):
            total += c[i][1] * mult
            cnt -= 1
            i += 1
            if cnt == 0:
                mult += 1
                cnt = 8

        return total
