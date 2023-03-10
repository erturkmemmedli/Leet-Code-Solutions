class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        two, three, five = 0, 0, 0
        while len(nums) < n:
            a, b, c = nums[two] * 2, nums[three] * 3, nums[five] * 5
            if a <= b and a <= c:
                nums.append(a)
                two += 1
                if a == b: three += 1
                if a == c: five += 1
            elif b < a and b <= c:
                nums.append(b)
                three += 1
                if b == c: five += 1
            elif c < a and c < b:
                nums.append(c)
                five += 1
        return nums[-1]

# Alternative solution (which gives TLE error)

class Solution1:
    def nthUglyNumber(self, n: int) -> int:
        self.goods = set()
        self.bads = set()
        i = 1
        while n:
            if self.recursion(i):
                self.goods.add(i)
                n -= 1
            else:
                self.bads.add(i)
            i += 1
        return i - 1

    def recursion(self, n):
        if n in self.goods:
            return True
        if n in self.bads:
            return False
        if n == 1:
            return True
        if n % 2 == 0:
            return self.recursion(n//2)
        elif n % 3 == 0:
            return self.recursion(n//3)
        elif n % 5 == 0:
            return self.recursion(n//5)
        return False
