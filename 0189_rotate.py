class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for _ in range(k):
            nums.insert(0, nums.pop())
            
# Alternative solution

class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
        nums[:] = nums[len(nums) - k % len(nums):] + nums[:len(nums) - k % len(nums)]

# Alternative solution

class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k >= len(nums): k = k % len(nums)
        if k == 0: return
        reserve = nums[-k:]
        for i in range(len(nums)-k-1,-1,-1):
            nums[i+k] = nums[i]
        for j in range(k):
            nums[j] = reserve[j]

# Alternative solution

class Solution3:
    def rotate(self, nums: List[int], k: int) -> None:
        l = len(nums)
        k = k % l
        if k == 0: return
        self.reverse(nums, 0, l-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, l-1)
        
    def reverse(self, nums, head, tail):
        while head < tail:
            nums[head], nums[tail] = nums[tail], nums[head]
            head += 1
            tail -= 1
