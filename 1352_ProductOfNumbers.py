class ProductOfNumbers:
    def __init__(self):
        self.preMult = [1]
        self.lastZero = None

    def add(self, num: int) -> None:
        if num != 0:
            self.preMult.append(num * self.preMult[-1])
        else:
            self.lastZero = len(self.preMult)

    def getProduct(self, k: int) -> int:
        if self.lastZero and len(self.preMult) - self.lastZero < k:
            return 0
        return self.preMult[-1] // self.preMult[len(self.preMult) - k - 1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

# Alternative solution (which gives TLE error)

class ProductOfNumbers1:
    def __init__(self):
        self.list = []

    def add(self, num: int) -> None:
        self.list.append(num)

    def getProduct(self, k: int) -> int:
        result = 1
        for i in range(len(self.list) - k, len(self.list)):
            result *= self.list[i]
        return result
