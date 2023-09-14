class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        frequency = {}
        count = 0
        for i, char in enumerate(s):
            if char not in frequency:
                frequency[char] = 1
            else:
                frequency[char] += 1
            if i >= k:
                frequency[s[i - k]] -= 1
                if not frequency[s[i - k]]:
                    del frequency[s[i - k]]
            if len(frequency) == k:
                count += 1
        return count
