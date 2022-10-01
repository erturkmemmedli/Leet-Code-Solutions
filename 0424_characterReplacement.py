class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        left = 0
        maximum = 0
        output = 0
        for right, char in enumerate(s):
            hashmap[char] = 1 + hashmap.get(char, 0)
            maximum = max(maximum, hashmap[char])
            if right - left - maximum >= k:
                hashmap[s[left]] -= 1
                left += 1
            output = max(output, right - left + 1)
        return output
