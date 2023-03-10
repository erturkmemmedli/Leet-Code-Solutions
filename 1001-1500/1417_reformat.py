class Solution:
    def reformat(self, s: str) -> str:
        digits = []
        letters = []
        for char in s:
            if 48 <= ord(char) <= 57:
                digits.append(char)
            if 97 <= ord(char) <= 122:
                letters.append(char)
        if abs(len(digits) - len(letters)) > 1:
            return ""
        string = ""
        if len(digits) != len(letters):
            digits, letters = max(digits, letters, key = len), min(digits, letters, key = len)
            string = digits.pop()
        while digits and letters:
            string += letters.pop()
            string += digits.pop()
        return string
