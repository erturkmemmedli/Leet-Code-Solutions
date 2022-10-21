class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window = collections.deque()
        total = 0
        length = inf
        i = 0
        while i < len(nums):
            if total < target:
                window.append(nums[i])
                total += nums[i]
                i += 1
            elif total == target:
                while total == target:
                    length = min(length, len(window))
                    total -= window.popleft()
                window.append(nums[i])
                total += nums[i]
                i += 1
            else:
                while total > target:
                    length = min(length, len(window))
                    total -= window.popleft()
        while total >= target:
            length = min(length, len(window))
            total -= window.popleft()
        return length if length != inf else 0
