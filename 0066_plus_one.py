class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        add = 1
        for i in range(len(digits)-1,-1,-1):
            if digits[i] == 9:
                digits[i] = (digits[i] + add) % 10
                if digits[i] == 0: add = 1
                else: add = 0
            else:
                if add == 1:
                    digits[i] += 1
                    add = 0
        if add == 1: digits.insert(0, 1)
        return digits
