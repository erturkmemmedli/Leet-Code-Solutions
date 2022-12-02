class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        n, difference, index, total = len(arr), float("inf"), -1, 0
        for i in range(n):
            if total + arr[i] * (n - i) == target:
                return arr[i]
            elif total + arr[i] * (n - i) < target:
                difference = abs(total + arr[i] * (n - i) - target)
                index = i
                total += arr[i]
            else:
                break
        newTarget = target - total
        denominator = n - index - 1
        if denominator == 0:
            return arr[-1]
        candidate, distance = divmod(newTarget, denominator)
        print(candidate, distance)
        return candidate if distance <= denominator // 2 else candidate + 1
