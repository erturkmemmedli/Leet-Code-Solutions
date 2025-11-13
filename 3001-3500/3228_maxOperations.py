class Solution:
    def maxOperations(self, s: str) -> int:
        ones = []
        current = ""
        total = 0

        for char in s:
            if char == '1':
                current += char
            elif current:
                ones.append(current)
                current = ""
        
        for i, one in enumerate(ones):
            total += len(one) * (len(ones) - i)

        return total
