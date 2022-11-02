class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        big, small, x, y, final = None, None, -1, -1, (-1, -1)
        for i, num in enumerate(arr):
            if big is None:
                big, x = arr[i], i
            elif small is None:
                if arr[i] >= big:
                    big, x = arr[i], i
                else:
                    small, y = arr[i], i
                    final = (x, y)
            elif arr[i] < small:
                big, small, x, y = small, arr[i], y, i
                final = (x, y)
            elif small < arr[i] < big:
                small, y = arr[i], i
                final = (x, y)
            elif big <= arr[i]:
                big, small, x, y = arr[i], None, i, -1
        if -1 not in final:
            a, b = final
            arr[a], arr[b] = arr[b], arr[a]
        return arr
