class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        i = 0
        j = 1
        k = math.inf
        while j < len(nums):
            if nums[j] > nums[j - 1]:
                i = j - 1
                k = math.inf
                j += 1
            else:
                if k == math.inf and nums[i] < nums[j] <= k:
                    k = j
                elif nums[i] < nums[j] <= nums[k]:
                    k = j
                j += 1
        if k == math.inf and nums[i] < nums[i + 1]:
            k = i + 1
        if k != math.inf: 
            nums[i], nums[k] = nums[k], nums[i]
            a = i + 1
            b = len(nums) - 1
            while a < b:
                nums[a], nums[b] = nums[b], nums[a]
                a += 1
                b -= 1
        else:
            a = i
            b = len(nums) - 1
            while a < b:
                nums[a], nums[b] = nums[b], nums[a]
                a += 1
                b -= 1
