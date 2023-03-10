class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0
        while j < len(typed) and i < len(name):
            if typed[j] == name[i]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j-1]:
                j += 1
            else:
                return False
        while j < len(typed):
            if typed[j] == typed[j-1]:
                j += 1
            else:
                return False
        if i < len(name):
            return False
        return True
