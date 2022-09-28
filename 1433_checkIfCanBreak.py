class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1, s2, i = sorted(s1), sorted(s2), 0
        while i < len(s1):
            if s1[i] == s2[i]:
                i += 1
                continue
            break
        s1, s2 = s1[i:], s2[i:]
        if not s1:
            return True
        return self.compare(s1, s2) if s1[0] < s2[0] else self.compare(s2, s1)
    
    def compare(self, first, second):
        for i in range(len(first)):
            if first[i] > second[i]:
                return False
        return True
