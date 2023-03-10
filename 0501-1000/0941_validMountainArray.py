class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        increase, has_increase, has_decrease = True, False, False
        for i in range(1, len(arr)):
            if increase:
                if arr[i] == arr[i-1]:
                    return False
                elif arr[i] > arr[i-1]:
                    has_increase = True
                else:
                    increase = False
                    has_decrease = True
            else:
                if arr[i] >= arr[i-1]:
                    return False
        return has_increase and has_decrease
