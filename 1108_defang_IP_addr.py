class Solution:
    def defangIPaddr(self, address: str) -> str:
        defanged = ''
        for ch in address:
            if ch != '.':
                defanged += ch
            else:
                defanged += '[.]'
        return defanged
