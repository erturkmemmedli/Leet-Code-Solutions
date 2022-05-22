class Solution:
    def countSubstrings(self, s):
        if s.count(s[0]) == len(s):
            return len(s) * (len(s) + 1) // 2
        count = 0
        i = 0
        while i < len(s):
            cut = s[:i+1]
            if cut.count(s[0]) == len(cut):
                count = len(cut) * (len(cut) + 1) // 2
            else:
                count = self.count_palindrom(cut, i, count)
            i += 1
        return count
            
    def count_palindrom(self, s, i, count):
        j = i
        temp = 0
        while j >= 0:
            while i - temp >= j + temp:
                if (i - j) % 2 == 0:
                    if s[i - temp] != s[j + temp]:
                        break
                    elif i - temp == j + temp:
                        count += 1
                        break
                    else:
                        temp += 1
                if (i - j) % 2 == 1:
                    if s[i - temp] != s[j + temp]:
                        break
                    elif i - temp == j + temp + 1:
                        count += 1
                        break
                    else:
                        temp += 1
            temp = 0
            j -= 1
        return count

# Alternative solution

class Solution1:
    def countSubstrings(self, s):
        count = 0
        for i in range(len(s)):
            for (a, b) in (i, i), (i, i + 1):
                while a >= 0 and b < len(s) and s[a] == s[b]:
                    a -= 1
                    b += 1
                count += (b - a) // 2
        return count
