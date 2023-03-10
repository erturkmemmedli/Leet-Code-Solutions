class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        nums.sort()
        one, two, three = [], [], 0
        for num in nums:
            if num % 3 == 1:
                one.append(num)
            elif num % 3 == 2:
                two.append(num)
            else:
                three += num
        # the case where all elements are used
        if len(one) % 3 == len(two) % 3:
            return three + sum(one) + sum(two)
        # the case where there is no element with mod 1
        if len(one) == 0:
            k = len(two) // 3
            return three + sum(two[len(two)-3*k:])
        # the case where there is no element with mod 2
        if len(two) == 0:
            k = len(one) // 3
            return three + sum(one[len(one)-3*k:])
        # if there are more ethan 4 elements, remove them and add to the total
        if len(one) > 4:
            one, three = self.calculate(one, three)
        if len(two) > 4:
            two, three = self.calculate(two, three)
        # last cases to consider
        if len(one) == len(two) + 2 or (len(one) == len(two) + 1 and len(one) > 2):
            return three + self.helper(two, one)
        if len(two) == len(one) + 2 or (len(two) == len(one) + 1 and len(two) > 2):
            return three + self.helper(one, two)
        else:
            return three + one[-1] + two[-1]

    def calculate(self, arr, total):
        if len(arr) % 3 == 2:
            total += sum(arr[2:])
            arr = arr[:2]
        elif len(arr) % 3 == 1:
            total += sum(arr[4:])
            arr = arr[:4]
        else:
            total += sum(arr[3:])
            arr = arr[:3]
        return arr, total

    def helper(self, one, two):
        return max(sum(two) + sum(one[len(one)-(len(two)-3):]), sum(two[-len(one):]) + sum(one))
