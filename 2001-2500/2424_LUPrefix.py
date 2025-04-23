class LUPrefix:

    def __init__(self, n: int):
        self.parent = list(range(n))
        self.uploaded = [False] * n

    def upload(self, video: int) -> None:
        self.uploaded[video - 1] = True
        if video < len(self.parent) and self.uploaded[video]:
            self.union(video - 1, video)
        if video - 1 > 0 and self.uploaded[video - 2]:
            self.union(video - 2, video - 1)

    def longest(self) -> int:
        return self.find(0) + 1 if self.uploaded[0] else 0
        
    def find(self, a):
        while a != self.parent[a]:
            a = self.parent[a]
        return a

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)

        if ra != rb:
            self.parent[ra] = rb

# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()
