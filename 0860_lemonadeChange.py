class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        stack_5 = []
        stack_10 = []
        for bill in bills:
            if bill == 5:
                stack_5.append(bill)
            if bill == 10:
                if not stack_5:
                    return False
                stack_5.pop()
                stack_10.append(bill)
            if bill == 20:
                if stack_10:
                    stack_10.pop()
                    if not stack_5:
                        return False
                    stack_5.pop()
                else:
                    if len(stack_5) < 3:
                        return False
                    for _ in range(3):
                        stack_5.pop()
        return True

# Alternative solution

class Solution1:
    def lemonadeChange(self, bills: List[int]) -> bool:
        stack_5 = 0
        stack_10 = 0
        for bill in bills:
            if bill == 5:
                stack_5 += 1
            if bill == 10:
                if not stack_5:
                    return False
                stack_5 -= 1
                stack_10 += 1
            if bill == 20:
                if stack_10:
                    stack_10 -= 1
                    if not stack_5:
                        return False
                    stack_5 -= 1
                else:
                    if len(stack_5) < 3:
                        return False
                    stack_5 -= 3
        return True
