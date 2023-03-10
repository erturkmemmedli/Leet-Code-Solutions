from collections import deque

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        error = deque()
        for i in range(len(nums)):
            if (i % 2 == 0 and nums[i] % 2 == 0) or (i % 2 == 1 and nums[i] % 2 == 1):
                continue
            else:
                error.append(i)
                if len(error) > 1:
                    if (nums[error[-1]] % 2 == 0 and nums[error[0]] % 2 == 1) or (nums[error[-1]] % 2 == 1 and nums[error[0]] % 2 == 0):
                        nums[error[-1]], nums[error[0]] = nums[error[0]], nums[error[-1]]
                        error.pop()
                        error.popleft()
        return nums

# Alternative solution

class Solution1:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = 0
        odd = 1
        while even < len(nums) and odd < len(nums):
            if nums[even] % 2 == 0:
                even += 2
            elif nums[odd] % 2 == 1:
                odd += 2
            else:
                nums[even], nums[odd] = nums[odd], nums[even]
                even += 2
                odd += 2
        return nums
