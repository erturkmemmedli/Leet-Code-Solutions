class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        for i in range(len(num)):
            if len(num) - 2*i - 1 == 1:
                return num[i] == num[len(num) - i - 1]
            elif len(num) - 2*i - 1 == 0:
                return True
            elif num[i] != num[len(num) - i - 1]:
                return False
				
# Alternative solution

class Solution1:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        start = 0
        end = len(str(x)) - 1
        while start < end:
            if x % 10 ** (end + 1) // 10 ** end != x % 10 ** (start + 1) // 10 ** start:
                return False
            start += 1
            end -= 1
        return True