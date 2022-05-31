class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        bin_count = 2 ** k
        hashset = set()
        for i in range(len(s) - k + 1):
            hashset.add(int(s[i:i+k], 2))
        for i in range(bin_count):
            if i not in hashset: return False
        return True
