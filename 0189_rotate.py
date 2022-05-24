class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for _ in range(k):
            nums.insert(0, nums.pop())
            
# Alternative solution

class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
        nums[:] = nums[len(nums) - k % len(nums):] + nums[:len(nums) - k % len(nums)]
