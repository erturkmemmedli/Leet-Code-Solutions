class TextEditor:
    def __init__(self):
        self.left_side = []
        self.right_side = deque()

    def addText(self, text: str) -> None:
        for char in text:
            self.left_side.append(char)

    def deleteText(self, k: int) -> int:
        count = 0
        while k > 0 and self.left_side:
            self.left_side.pop()
            count += 1
            k -= 1
        return count

    def cursorLeft(self, k: int) -> str:
        for _ in range(min(k, len(self.left_side))):
            char = self.left_side.pop()
            self.right_side.appendleft(char)
        substring = self.left_side[-10:] if len(self.left_side) > 10 else self.left_side
        return "".join(substring)

    def cursorRight(self, k: int) -> str:
        for _ in range(min(k, len(self.right_side))):
            char = self.right_side.popleft()
            self.left_side.append(char)
        substring = self.left_side[-10:] if len(self.left_side) > 10 else self.left_side
        return "".join(substring)


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
