class Solution:
    def minimumSum(self, num: int) -> int:
        num = str(num)
        minimum = min(
            int(num[0]) + int("".join(sorted(ch for ch in num[1:]))),
            int(num[1]) + int("".join(sorted(ch for ch in num[0] + num[2:]))),
            int(num[2]) + int("".join(sorted(ch for ch in num[:2] + num[3]))),
            int(num[3]) + int("".join(sorted(ch for ch in num[:3]))),
            int("".join(sorted(ch for ch in num[:2]))) + int("".join(sorted(ch for ch in num[2:]))),
            int("".join(sorted(ch for ch in num[0] + num[2]))) + int("".join(sorted(ch for ch in num[1] + num[3]))),
            int("".join(sorted(ch for ch in num[0] + num[3]))) + int("".join(sorted(ch for ch in num[1] + num[2])))
        )

        return minimum
