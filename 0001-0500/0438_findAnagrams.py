class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return
        target = collections.Counter(p)
        source = Counter(s[0:len(p)])
        result = []
        if source == target:
            result.append(0)
        for i in range(len(p), len(s)):
            source[s[i - len(p)]] -= 1
            source[s[i]] += 1
            if source == target:
                result.append(i - len(p) + 1)
        return result

# Alternative solution

class Solution:
    def findAnagrams(self, s, p):
        if len(s) < len(p):
            return []
        k = len(p)
        anagrams = []
        frequency = {}
        headWindow = 0
        for char in p:
            if char not in frequency:
                frequency[char] = 1
            else:
                frequency[char] += 1
        for i, char in enumerate(s):
            if char in frequency:
                frequency[char] -= 1
                if not frequency[char]:
                    del frequency[char]
            else:
                frequency[char] = -1
            if i == k - 1:
                if not frequency:
                    anagrams.append(0)
            elif i >= k:
                if s[headWindow] not in frequency:
                    frequency[s[headWindow]] = 1
                else:
                    frequency[s[headWindow]] += 1
                    if not frequency[s[headWindow]]:
                        del frequency[s[headWindow]]
                if not frequency:
                    anagrams.append(headWindow + 1)
                headWindow += 1
        return anagrams
