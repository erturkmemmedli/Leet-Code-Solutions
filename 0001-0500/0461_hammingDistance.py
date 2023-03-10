class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bit_x = bin(x)[2:]
        bit_y = bin(y)[2:]
        if len(bit_x) < len(bit_y):
            bit_x = '0' * (len(bit_y)-len(bit_x)) + bit_x
        if len(bit_x) > len(bit_y):
            bit_y = '0' * (len(bit_x)-len(bit_y)) + bit_y
        hamming_distance = 0
        for i in range(len(bit_x)):
            if bit_x[i] != bit_y[i]:
                hamming_distance += 1
        return hamming_distance
      
# Alternative solution

class Solution1:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        while x or y:
            if x % 2 != y % 2:
                count += 1
            x = x >> 1
            y = y >> 1
        return count
    
# Alternative solution

class Solution2:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        count = 0
        while xor:
            if xor & 1:
                count += 1
            xor >>= 1
        return count
