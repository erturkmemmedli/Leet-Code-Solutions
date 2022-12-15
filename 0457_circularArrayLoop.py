class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        self.visited = set()
        self.illegal = set()
        for i, step in enumerate(nums):
            if i not in self.visited:
                self.path = set()
                self.traverse(nums, i)
                if len(self.path) > 1:
                    return True
        return False
        
    def traverse(self, nums, index):
        newIndex = (index + nums[index]) % len(nums)
        if index == newIndex or index in self.illegal  or (nums[index] < 0 and nums[newIndex] > 0) or (nums[index] > 0 and nums[newIndex] < 0):
            for num in self.path:
                self.illegal.add(num)
            self.path = set()
            return False
        elif index not in self.path and index not in self.illegal:
            self.visited.add(index)
            self.path.add(index)
            if self.traverse(nums, (index + nums[index]) % len(nums)):
                return True
