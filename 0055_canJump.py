class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mxm_dist = mxm_dist=0
        for i in range(len(nums) - 1):
            mxm_dist = max(mxm_dist - 1, nums[i])
            if mxm_dist == 0:
                return False
        return True

# Alternative solution (which gives TLE error)

class Solution1:
    def canJump(self, nums: List[int]) -> bool:
        bfsQueue = collections.deque([(0, nums[0])])
        while bfsQueue:
            index, distance = bfsQueue.popleft()
            if index == len(nums) - 1:
                return True
            for i in range(distance, 0, -1):
                if index + i == len(nums) - 1 or (index + i < len(nums) and nums[index + i] != 0):
                    bfsQueue.append((index + i, nums[index + i]))
        return False

# Alternative colution

class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                return False
            mxm = nums[i]
            for j in range(i + 1, i + nums[i] + 1):
                if j + nums[j] >= len(nums) - 1:
                    return True
                if j + nums[j] >= mxm:
                    mxm = j + nums[j]
                    i = j
        return True

# Alterntaive solution

class Solution3:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        travel = 0
        for i in range(len(nums) - 1):
            if nums[i] == 0:
                if travel <= i:
                    return False
            travel = max(travel, i + nums[i])
            if travel >= len(nums) - 1: return True
        return False
