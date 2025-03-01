class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = nums
        if not (a + b > c and a + c > b and b + c > a):
            return "none"
        elif a == b == c:
            return "equilateral"
        elif a == b or b == c or a == c:
            return "isosceles"
        else:
            return "scalene"
