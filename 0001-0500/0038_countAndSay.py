class Solution:
    def countAndSay(self, n: int) -> str:
        return self.recursive(n, "1")

    def recursive(self, n, s):
        if n == 1:
            return s
        output = ""
        last_element = s[0]
        count = 1
        for i in range(1, len(s)):
            if s[i] == last_element:
                count += 1
            else:
                output += str(count) + last_element
                last_element = s[i]
                count = 1
        output += str(count) + last_element
        return self.recursive(n - 1, output)
