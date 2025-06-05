class Solution:
    def isNumber(self, s: str) -> bool:
        if 'inf' in s or 'Inf' in s or 'nan' in s:
            return False

        try:
            _ = float(s)
        except:
            return False
            
        return True
