class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        length = 0
        for char in s:
            length = length * int(char) if char.isdigit() else length + 1
        for char in reversed(s):
            k %= length
            if k == 0 and char.isalpha():
                return char
            length = length // int(char) if char.isdigit() else length - 1
