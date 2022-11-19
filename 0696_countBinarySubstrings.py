class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        total = 0
        count1 = 0
        count2 = 0
        i = 0
        j = 0
        while j < len(s):
            if s[i] == s[j]:
                if count2 != 0:
                    total += min(count1, count2)
                    i += count1
                    count1 = count2
                    count2 = 0
                else:
                    count1 += 1
                    j += 1
            else:
                count2 += 1
                j += 1
        total += min(count1, count2)
        return total
