from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s = Counter(secret)
        g = Counter(guess)
        common = s - (s - g)
        commonCount = sum(common.values())
        sameLocation = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                sameLocation += 1
        differenLocation = commonCount - sameLocation
        return str(sameLocation) + 'A' + str(differenLocation) + 'B'
