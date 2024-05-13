class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        parts = s.split('-')
        joined = "".join(parts).upper()

        div, mod = divmod(len(joined), k)
        output = joined[:mod]

        for i in range(mod, len(joined), k):
            if output:
                output += '-'
            
            output += joined[i : i + k]
        
        return output
