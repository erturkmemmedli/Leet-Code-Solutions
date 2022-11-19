class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        perm = []
        I = 0
        D = len(s)
        for i in range(D):
            if s[i] == 'I':
                perm.append(I)
                I += 1
            if s[i] == 'D':
                perm.append(D)
                D -= 1
        perm.append(I)
        return perm
