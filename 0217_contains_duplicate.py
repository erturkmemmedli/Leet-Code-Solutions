class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num not in hashset:
                hashset.add(num)
            else:
                return True
        return False

# Alternative solution

class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
