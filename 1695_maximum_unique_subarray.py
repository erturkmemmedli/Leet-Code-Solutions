from collections import deque

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        queue = deque()
        myset = set()
        temp = 0
        result = 0
        for num in nums:
            if num not in myset:
                myset.add(num)
                queue.append(num)
                temp += num
                result = max(temp, result)
            else:
                while num in myset:
                    pop = queue.popleft()
                    temp -= pop
                    myset.remove(pop)
                myset.add(num)
                queue.append(num)
                temp += num
                result = max(temp, result)
        return result
