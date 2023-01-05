class Solution:
    def numSub(self, s: str) -> int:
        contiguousOnes = []
        count = 0
        for char in s:
            if char == '1':
                count += 1
            else:
                if count: contiguousOnes.append(count)
                count = 0
        if count: contiguousOnes.append(count)
        result = 0
        for num in contiguousOnes:
            result += num * (num + 1) // 2
        return result % 1_000_000_007
