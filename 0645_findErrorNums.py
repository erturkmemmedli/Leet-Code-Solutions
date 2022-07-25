class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        output = []
        s = set()
        for num in nums:
            if num not in s:
                s.add(num)
            else:
                output.append(num)
        for i in range(1, len(nums)+1):
            if i not in s:
                output.append(i)
                break
        return output
