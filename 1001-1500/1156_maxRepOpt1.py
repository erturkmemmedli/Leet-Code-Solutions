class Solution:
    def maxRepOpt1(self, text: str) -> int:
        hashmap = {}
        for i in range(len(text)):
            if text[i] not in hashmap:
                hashmap[text[i]] = [1]
            else:
                if text[i] == text[i - 1]:
                    hashmap[text[i]][-1] += 1
                else:
                    if text[i] == text[i - 2]:
                        hashmap[text[i]].append(1)
                    else:
                        hashmap[text[i]].append(0)
                        hashmap[text[i]].append(1)
        longestLength = 1
        for k, v in hashmap.items():
            if len(v) == 1:
                longestLength = max(longestLength, v[0])
            elif len(v) == 2:
                longestLength = max(longestLength, v[0] + v[1])
            else:
                for i in range(len(v) - 1):
                    longestLength = max(longestLength, v[i] + v[i + 1] + 1)
        return longestLength
