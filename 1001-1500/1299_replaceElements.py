class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        temp = arr[-1]
        curr = temp
        arr[-1] = -1
        for i in range(len(arr)-2, -1, -1):
            temp = max(temp, curr)
            curr = arr[i]
            arr[i] = temp
        return arr
