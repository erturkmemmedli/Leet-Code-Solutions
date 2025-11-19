class Solution:
    def kthCharacter(self, k: int) -> str:
        n = 10
        final = "a"

        while n > 0:
            original = final
            generated = ""

            for char in original:
                generated += chr(ord('a') + (ord(char) - ord('a') + 1) % 26)
            
            final = original + generated
            n -= 1

        return final[k - 1]
