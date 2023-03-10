class Solution:
    def compress(self, chars: List[str]) -> int:
        char = chars[0]
        count = 1
        position = 0
        i = 1

        while i < len(chars):
            if chars[i] == char:
                count += 1
            else:
                chars[position] = char
                position = self.appendDigit(chars, count, position + 1)
                char = chars[i]
                count = 1
            i += 1

        chars[position] = char
        position = self.appendDigit(chars, count, position + 1)
        return position

    def appendDigit(self, chars, count, position):
        if 1 < count < 10:
            chars[position] = str(count)
            position += 1
        elif count >= 10:
            for digit in str(count):
                chars[position] = digit
                position += 1
        return position
