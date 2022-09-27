class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        position_of_one = -float(inf)
        i = 0
        while i < len(nums):
            if nums[i] == 1:
                if i - position_of_one > k:
                    position_of_one = i
                    i += 1
                else:
                    return False
            else:
                i += 1
        return True
