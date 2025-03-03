class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        greater = []
        count = 0

        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                count += 1
            else:
                greater.append(num)

        return less + [pivot] * count + greater
