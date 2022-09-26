from collections import deque

class BrowserHistory:
    def __init__(self, homepage: str):
        self.current = homepage
        self.back_stack = []
        self.forward_queue = deque()

    def visit(self, url: str) -> None:
        self.back_stack.append(self.current)
        self.forward_queue = deque()
        self.current = url

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.back_stack:
                self.forward_queue.appendleft(self.current)
                self.current = self.back_stack.pop()
            else:
                break
        return self.current

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.forward_queue:
                self.back_stack.append(self.current)
                self.current = self.forward_queue.popleft()
            else:
                break
        return self.current

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
