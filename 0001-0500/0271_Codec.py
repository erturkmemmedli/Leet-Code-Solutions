class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""

        for string in strs:

            for letter in string:
                ascii_form = str(ord(letter))
                final_form = "0" * (3 - len(ascii_form)) + ascii_form
                res += final_form

            res += " " * 3

        return res
                
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        out = []
        word = ""

        for i in range(0, len(s), 3):
            new = s[i:i+3]

            if new != "   ":
                word += chr(int(new))
            else:
                out.append(word)
                word = ""

        return out


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
