from collections import defaultdict as D

class Solution:
    def numDecodings(self, s: str) -> int:
        numMap = {str(i) for i in range(1, 27)}
        decodeMap = D(int, {s[0]: 1}) if s[0] != '0' else D(int)
        for num in s[1:]:
            if not decodeMap: return 0
            temp = D(int)
            for key, val in decodeMap.items():
                if key + num in numMap:
                    temp[key + num] += val
                if num in numMap:
                    temp[num] += val
            decodeMap = temp
        return sum(decodeMap.values())
