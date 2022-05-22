class Solution:
    def countSubstrings(self, s):
        if s.count(s[0]) == len(s):
            return len(s) * (len(s) + 1) // 2
        count = 0
        i = 0
        while i < len(s):
            count = self.count_palindrom(s[:i+1], i, count)
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
