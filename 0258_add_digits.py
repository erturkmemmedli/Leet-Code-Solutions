class Solution:
    def addDigits(self, num: int) -> int:
        while num > 10:
            num = sum(list(map(int, list(str(num)))))
        return num
      
# Alternative solution

class Solution1:
    def addDigits(self, num: int) -> int:
        return 0 if not num else 9 if not num % 9 else num % 9
