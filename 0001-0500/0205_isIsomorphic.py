class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}
        for i in range(len(s)):
            if s[i] not in hash_s:
                hash_s[s[i]] = t[i]
            else:
                if hash_s[s[i]] != t[i]:
                    return False
            if t[i] not in hash_t:
                hash_t[t[i]] = s[i]
            else:
                if hash_t[t[i]] != s[i]:
                    return False
        return True
