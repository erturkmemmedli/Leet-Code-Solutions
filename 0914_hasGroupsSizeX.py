from collections import Counter

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        liste = list(Counter(deck).values())
        if 1 in liste: return False
        if len(set(liste)) == 1: return True
        gcd = liste[0]
        for i in range(1, len(liste)):
            if gcd == liste[i]:
                continue
            else:
                new = self.gcd(max(gcd, liste[i]), min(gcd, liste[i]))
                if new:
                    gcd = min(gcd, new)
                else:
                    return False
        return True         

    def gcd(self, a, b):
        while b > 1:
            a, b = b, a % b
        if b == 0:
            return a
        else:
            return 0
