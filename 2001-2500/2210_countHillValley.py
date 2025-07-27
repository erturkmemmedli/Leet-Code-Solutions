class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        stack = []
        answer = 0

        for num in nums:
            if not stack or stack[-1] != num:
                stack.append(num)
        
        for i in range(1, len(stack) - 1):
            if (stack[i-1] < stack[i] > stack[i+1]) or (stack[i-1] > stack[i] < stack[i+1]):
                answer += 1

        return answer
