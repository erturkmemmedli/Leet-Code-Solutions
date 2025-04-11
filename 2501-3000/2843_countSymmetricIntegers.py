class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        i = low
        while i <= high:
            s = str(i)
            l = len(s)
            
            if l % 2 != 0:
                i = int('1' + '0' * l)
            
            if sum([int(c) for c in s[:l//2]]) == sum([int(c) for c in s[l//2:]]):
                count += 1
            
            i += 1

        return count
