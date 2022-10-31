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
