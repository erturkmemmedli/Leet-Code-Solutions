class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        increase, prev, curr, result = True, 0, 0, 0
        for num in target:
            if not curr:
                curr = num
                continue
            if increase:
                if num < curr:
                    increase = False
                prev, curr = curr, num
            else:
                if num <= curr:
                    curr = num
                else:
                    increase = True
                    result += prev - curr
                    prev, curr = curr, num
        result += curr if increase else prev
        return result
