class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        count = 0
        for num in nums:
            if num:
                product *= num
            else:
                count += 1
        if count > 1:
            return [0] * len(nums)
        elif count == 1:
            return [0 if num else product for num in nums]
        elif count == 0:
            return [product // nums[i] for i in range(len(nums))]
