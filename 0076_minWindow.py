class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        minLength = float("inf")
        substring = ""
        left = 0
        tMap = {}
        for char in t:
            tMap[char] = 1 if char not in tMap else tMap[char] + 1
        sMap = {}
        for right, char in enumerate(s):
            if char not in tMap:
                continue
            if char not in sMap:
                sMap[char] = 1
            else:
                sMap[char] += 1
            while len(sMap) == len(tMap) and all(tMap[key] <= sMap[key] for key in tMap):
                if minLength > right - left + 1:
                    minLength = right - left + 1
                    substring = s[left: right + 1]
                if s[left] in sMap:
                    sMap[s[left]] -= 1
                    if sMap[s[left]] == 0:
                        del sMap[s[left]]
                left += 1
        return substring

# Alternative solution

class Solution1:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        frequency = {}
        for char in t:
            if char not in frequency:
                frequency[char] = 0
            frequency[char] += 1
        left = 0
        startIndex = 0
        matched = 0
        minLength = float("inf")
        for right, char in enumerate(s):
            if char in frequency:
                frequency[char] -= 1
                if frequency[char] == 0:
                    matched += 1
                while matched == len(frequency):
                    if minLength > right - left + 1:
                        minLength = right - left + 1
                        startIndex = left
                    if s[left] in frequency:
                        if frequency[s[left]] == 0:
                            matched -= 1
                        frequency[s[left]] += 1
                    left += 1
        return s[startIndex : startIndex + (minLength if minLength != float("inf") else 0)]
