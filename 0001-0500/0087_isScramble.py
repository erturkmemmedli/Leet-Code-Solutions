class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        self.memo = {}
        return self.recursion(s1, s2)

    def recursion(self, s1, s2):
        if s1 == s2:
            return True

        if Counter(s1) != Counter(s2):
            return False
        
        if (s1, s2) in self.memo:
            return self.memo[(s1, s2)]

        self.memo[(s1, s2)] = False

        for i in range(1, len(s1)):
            if self.recursion(s1[:i], s2[:i]) and self.recursion(s1[i:], s2[i:]):
                self.memo[(s1, s2)] = True
                return True

            if self.recursion(s1[:i], s2[-i:]) and self.recursion(s1[i:], s2[:-i]):
                self.memo[(s1, s2)] = True
                return True

        return self.memo[(s1, s2)]
