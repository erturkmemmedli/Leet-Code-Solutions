class Solution:
    def arrayRankTransform(self, arr):
        sorted_arr = sorted(arr)
        k = 1
        dic = {}
        for i in range(len(sorted_arr)):
            if sorted_arr[i] not in dic:
                dic[sorted_arr[i]] = k
                k += 1
        for i in range(len(arr)):
            arr[i] = dic[arr[i]]
        return arr
