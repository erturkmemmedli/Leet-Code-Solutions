class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        l = len(palindrome)
        n = math.ceil(l/2)
        idx = -1
        for i in range(n):
            if palindrome[i] != 'a':
                idx = i
                break
        if l > 1 and (idx == -1 or (idx != -1 and l%2 == 1 and idx == l//2)):
            return  palindrome[:-1] + 'b'
        elif l > 1 and idx != -1:
            return palindrome[:idx] + 'a' + palindrome[idx+1:]
        else:
            return ""
