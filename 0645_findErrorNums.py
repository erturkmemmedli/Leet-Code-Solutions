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

# Alternative solution

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        for i, num in enumerate(nums):
            if num != i + 1:
                return [num, i + 1]
