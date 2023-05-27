class Solution:
    def confusingNumber(self, n: int) -> bool:
        temp = n
        digits = []
        
        while temp:
            x = temp % 10
            digits.append(x)
            temp //= 10
            
        non_confusing = {2,3,4,5,7}
        
        for d in digits:
            if d in non_confusing:
                return False
        
        i = 0
        j = len(digits) - 1
                        
        while i <= j:
            if digits[i] != digits[j]:
                if (digits[i] == 6 and digits[j] == 9) or (digits[i] == 9 and digits[j] == 6):
                    i += 1
                    j -= 1
                else:
                    return True

            else:
                if digits[i] == 6 or digits[i] == 9:
                    return True
                else:
                    i += 1
                    j -= 1
                
        return False
