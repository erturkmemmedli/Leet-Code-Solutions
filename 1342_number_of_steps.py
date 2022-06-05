class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 2 == 1:
            return 1 + self.numberOfSteps(num - 1)
        if num % 2 == 0:
            return 1 + self.numberOfSteps(num // 2)

# Alternative solution

class Solution1:
    def numberOfSteps(self, num: int) -> int:
        bitstring = bin(num)[2:]
        return len(bitstring) - 1 + bitstring.count('1')

# Alternative solution 

class Solution2:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num:
            if num % 2 == 1:
                num -= 1
                count += 1
            elif num % 2 == 0:
                num = num >> 1
                count += 1
        return count
