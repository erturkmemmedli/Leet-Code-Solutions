class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        j = 0
        for i in range(1, target[-1] + 1):
            if target[j] == i:
                stack.append('Push')
                j += 1
            else:
                stack.append('Push')
                stack.append('Pop')
        return stack
