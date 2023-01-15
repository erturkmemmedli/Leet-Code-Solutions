class Solution:
    def defangIPaddr(self, address: str) -> str:
        defanged = ''
        for ch in address:
            if ch != '.':
                defanged += ch
            else:
                defanged += '[.]'
        return defanged

# Alternative solution

class Solution:
    def defangIPaddr(self, address):
        defanged = ""
        for char in address:
            defanged += char if char.isdigit() else '[.]'
        return defanged
