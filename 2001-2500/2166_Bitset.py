class Bitset:
    def __init__(self, size: int):
        self.bits = 0
        self.size = size
        self.ones = 0

    def fix(self, idx: int) -> None:
        fixed = self.bits | (1 << (self.size - idx - 1))
        if self.bits != fixed:
            self.ones += 1
            self.bits = fixed
        
    def unfix(self, idx: int) -> None:
        unfixed = (1 << (self.size - idx - 1))
        if self.bits & unfixed:
            self.bits -= unfixed
            self.ones -= 1

    def flip(self) -> None:
        self.bits ^= ((1 << self.size) - 1)
        self.ones = self.size - self.ones

    def all(self) -> bool:
        return self.ones == self.size #self.bits == ((1 << self.size) - 1)

    def one(self) -> bool:
        return self.ones > 0 #self.bits != 0

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        res = bin(self.bits)[2:]
        return "0" * (self.size - len(res)) + res

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()

# Alternative solution (which gives TLE error)

class Bitset:
    def __init__(self, size: int):
        self.bits = [0] * size

    def fix(self, idx: int) -> None:
        self.bits[idx] = 1

    def unfix(self, idx: int) -> None:
        self.bits[idx] = 0

    def flip(self) -> None:
        for i in range(len(self.bits)): self.bits[i] ^= 1

    def all(self) -> bool:
        return all(bit == 1 for bit in self.bits)

    def one(self) -> bool:
        return any(bit == 1 for bit in self.bits)

    def count(self) -> int:
        return sum(bit == 1 for bit in self.bits)

    def toString(self) -> str:
        return "".join(str(bit) for bit in self.bits)
