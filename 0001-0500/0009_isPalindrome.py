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

# Alternative solution

class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        n = x
        head = -1
        while n:
            n = n // 10
            head += 1
        tail = 1
        while tail <= head:
            if x // 10 ** head % 10 != x % 10 ** tail // 10 ** (tail - 1): return False
            tail += 1
            head -= 1
        return True

# Alternative solution

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        s = str(x)
        return s == s[::-1]
