class Solution:
    def calculate(self, s: str) -> int:
        nums = []
        temp = ""
        operation = None
        for i in range(len(s)):
            if s[i] == ' ':
                continue
            if 48 <= ord(s[i]) <= 57:
                temp += s[i]
            else:
                temp = self.helper(nums, operation, temp)
                operation = s[i]
        self.helper(nums, operation, temp)
        return sum(nums)

    def helper(self, nums, operation, temp):
        if not operation:
            nums.append(int(temp))
        elif operation == '+':
            nums.append(int(temp))
        elif operation == '-':
            nums.append(-int(temp))
        elif operation == '*':
            nums[-1] *= int(temp)
        elif operation == '/':
            if nums[-1] < 0:
                nums[-1] = -(-nums[-1] // int(temp))
            else:
                nums[-1] //= int(temp)
        return ""
