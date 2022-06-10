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
