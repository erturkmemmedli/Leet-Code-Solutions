class Solution:
    def balancedString(self, s: str) -> int:
        length = len(s)
        countOneLetter = length // 4
        countMap = collections.Counter(s)
        windowMap = {}
        for char in countMap:
            if countMap[char] > countOneLetter:
                windowMap[char] = countMap[char] - countOneLetter
        if not windowMap:
            return 0
        matched = 0
        left = 0
        minLengthForBalance = length - 1
        for right, char in enumerate(s):
            if char in windowMap:
                windowMap[char] -= 1
                if windowMap[char] == 0:
                    matched += 1
                while matched == len(windowMap):
                    minLengthForBalance = min(minLengthForBalance, right - left + 1)
                    if s[left] in windowMap:
                        windowMap[s[left]] += 1
                        if windowMap[s[left]] > 0:
                            matched -= 1
                    left += 1
        return minLengthForBalance
