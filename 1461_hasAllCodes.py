class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        bin_count = 2 ** k
        hashset = set()
        for i in range(len(s) - k + 1):
            hashset.add(int(s[i:i+k], 2))
        for i in range(bin_count):
            if i not in hashset: return False
        return True

# Alternative solution

class Solution1:
    def hasAllCodes(self, s: str, k: int) -> bool:
        hashset = set()
        for i in range(0, len(s)-k+1):
            hashset.add(s[i:i+k])
        return len(hashset) == 2 ** k

# Alternative solution

class Solution2:
    def hasAllCodes(self, s: str, k: int) -> bool:
        total = 1 << k
        isContained = set()
        binaryOnes = total - 1
        hashValue = 0
        for i in range(len(s)):
            hashValue = (hashValue << 1) & binaryOnes | int(s[i])
            if i >= k - 1 and hashValue not in isContained:
                isContained.add(hashValue)
                total -= 1
                if total == 0:
                    return True
        return False
