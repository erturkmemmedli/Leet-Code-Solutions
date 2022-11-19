class NumArray:
    def __init__(self, nums: List[int]):
        self.array = nums

    def sumRange(self, left: int, right: int) -> int:
        summ = 0
        for i in range(left, right+1):
            summ += self.array[i]
        return summ

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# Alternative solution

class NumArray1:
    def __init__(self, nums: List[int]):
        self.array = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.array[left:right+1])
      
# Alternative solution

class NumArray2:
    def __init__(self, nums: List[int]):
        self.array = [0]
        for i in range(len(nums)):
            self.array.append(nums[i] + self.array[-1])

    def sumRange(self, left: int, right: int) -> int:
        return self.array[right+1] - self.array[left]
