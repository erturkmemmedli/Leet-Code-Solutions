from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashmap = Counter(text)
        minimum = float('inf')
        liste = [hashmap[k] for k in 'loban']
        liste[0], liste[1] = liste[0] // 2, liste[1] // 2
        return min(liste)
