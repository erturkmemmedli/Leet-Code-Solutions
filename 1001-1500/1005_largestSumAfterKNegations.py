class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        for i in range(len(nums)):
            if k == 0:
                break
            if nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1
            elif nums[i] == 0:
                k = 0
                break
            else:
                if k % 2 != 0:
                    if i and nums[i-1] < nums[i]:
                        nums[i-1] = -nums[i-1]
                    else:
                        nums[i] = -nums[i]
                k = 0
                break
        if k and k % 2 != 0:
            nums[-1] = -nums[-1]
        return sum(nums)                           

# Alternative solution

import heapq

class Solution1:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while k > 0:
            pop = heapq.heappop(nums)
            if pop < 0:
                heapq.heappush(nums, -pop)
                k -= 1
            elif pop == 0:
                break
            else:
                if k % 2 == 0:
                    heapq.heappush(nums, pop)
                    break
                else:
                    heapq.heappush(nums, -pop)
                    break
        return sum(nums)
