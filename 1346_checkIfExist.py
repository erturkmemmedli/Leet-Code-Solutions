class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        sett = set(arr)
        for num in arr:
            if num == 0:
                if arr.count(0) > 1: return True
            else:
                if num * 2 in sett: return True
                if num % 2 == 0 and num // 2 in sett: return True
        return False
