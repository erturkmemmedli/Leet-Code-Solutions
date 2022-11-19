class Solution:
    def freqAlphabets(self, s: str) -> str:
        string = ""
        i = 0
        while i < len(s):
            if i < len(s) - 2:
                if s[i+2] == '#':
                    string += chr(96 + int(s[i:i+2]))
                    i += 3
                else:
                    string += chr(96 + int(s[i]))
                    i += 1
            else:
                string += chr(96 + int(s[i]))
                i += 1
        return string
