class Solution:
    def __init__(self, w: List[int]):
        tot = sum(w)
        self.weights = []
        for i in range(len(w)):
            self.weights += [i] * int(w[i] / tot * 10000)

    def pickIndex(self) -> int:
        return random.choice(self.weights)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
