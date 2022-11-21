class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        window = collections.deque()
        result = 0
        count = 0
        flag = False
        provider = 1
        for num in nums:
            if goal == 0:
                if num == 0:
                    result += provider
                    provider += 1
                else:
                    provider = 1
            else:
                if count < goal:
                    window.append(num)
                    if not flag and num == 1:
                        flag = True
                    if not flag:
                        provider += 1
                    if num == 1:
                        count += 1
                    if count == goal:
                        while window and window[0] != 1:
                            window.popleft()
                        result += provider
                    continue
                if num == 0:
                    result += provider
                    window.append(num)
                else:
                    window.popleft()
                    provider = 1
                    while window and window[0] != 1:
                        window.popleft()
                        provider += 1
                    result += provider
                    window.append(num)
        return result
