class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        binary = ""
        result = []
        for num in nums:
            binary += str(num)
            if int(binary, 2) % 5 == 0:
                result.append(True)
            else:
                result.append(False)
        return result
      
# Alternative solution

class Solution1:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        decimal = 0
        result = []
        for num in nums:
            if num == 0:
                decimal = decimal * 2
            else:
                decimal = decimal * 2 + 1 
            if decimal % 5 == 0:
                result.append(True)
            else:
                result.append(False)
        return result
