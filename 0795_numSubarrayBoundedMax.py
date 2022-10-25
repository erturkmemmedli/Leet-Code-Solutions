class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        total = 0
        problem = 0
        start = 0
        mark = False
        small = 0
        i = 0
        while i < len(nums):
            if nums[i] < left:
                if not mark:
                    mark = True
                    small = i
            elif nums[i] <= right:
                if mark:
                    n = i - small
                    problem += n * (n + 1) // 2
                    mark = False
            else:
                if mark:
                    n = i - small
                    problem += n * (n + 1) // 2
                    mark = False
                m = i - start
                total += m * (m + 1) // 2
                start = i + 1
            i += 1
        if mark:
            n = i - small
            problem += n * (n + 1) // 2
        m = i - start
        total += m * (m + 1) // 2
        return total - problem
