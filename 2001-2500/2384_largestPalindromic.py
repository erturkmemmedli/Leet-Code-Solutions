class Solution:
    def largestPalindromic(self, num: str) -> str:
        letter_map = Counter(num)
        middle = None

        for char in sorted(letter_map.keys(), reverse=True):
            if letter_map[char] % 2 == 1:
                middle = char
                break
            
        result = ""

        for char in sorted(letter_map.keys(), reverse=True):
            result += char * (letter_map[char] // 2)

        if middle:
            result += middle

        for char in sorted(letter_map.keys()):
            result += char * (letter_map[char] // 2)

        result = result.strip('0')
        return result if result else "0"
