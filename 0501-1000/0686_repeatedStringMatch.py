class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if len(a) >= len(b):
            string = b + '$' + a + a
            index = self.kmp(string, len(b))
            return -1 if index == -1 else 1 if index + len(b) <= len(a) else 2
        count = 0
        a_new = ""
        while len(a_new) < len(b) + len(a):
            a_new += a
            count += 1
        string = b + '#' + a_new
        index = self.kmp(string, len(b)) 
        return -1 if index == -1 else count if index + len(b) > len(a_new) - len(a) else count - 1

    def kmp(self, s, n):
        l = len(s)
        prefix = [0] * l
        j = 0
        for i in range(1, l):
            while j > 0 and s[i] != s[j]:
                j = prefix[j-1]
            if s[i] == s[j]:
                j += 1
            else:
                j = 0
            prefix[i] = j
            if prefix[i] == n:
                return i - 2 * n
        return -1

# Alternative solution

class Solution1:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        temp, count = "", 0
        while len(temp) < len(a) + len(b):
            temp += a
            count += 1
            if b in temp:
                return count
        return -1
