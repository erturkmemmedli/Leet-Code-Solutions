class Solution:
    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.hashmap = {}
        self.total = m * n

    def flip(self) -> List[int]:
        val = random.randint(0, self.total - 1)
        self.total -= 1
        x = self.hashmap.get(val, val)
        self.hashmap[val] = self.hashmap.get(self.total, self.total)
        return [x // self.n, x % self.n]

    def reset(self) -> None:
        self.hashmap.clear()
        self.total = self.m * self.n

# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()
