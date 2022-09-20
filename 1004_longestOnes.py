class Solution

# Alternative solution (which gives TLE error)

class Solution1:
    def longestOnes(self, nums: List[int], k: int) -> int:
        arr, count, flag = [], 0, 0
        for num in nums:
            if num ^ flag:
                count += 1
            else:
                arr.append(count)
                flag ^= 1
                count = 1
        arr.append(count)
        mxm, curr, temp, i, step = arr[0], arr[0], k, 1, 0
        while i < len(arr):
            if arr[i] <= temp:
                curr += arr[i]
                if i + 1 < len(arr):
                    curr += arr[i + 1]
                mxm = max(mxm, curr)
                temp -= arr[i]
                i += 2
                step += 1
            elif temp == k:
                mxm = max(mxm, temp + arr[i - 1])
                if i + 1 < len(arr):
                    mxm = max(mxm, temp + arr[i + 1])
                i += 2
            else:
                if step > 1:
                    i -= 2 * (step - 1)
                mxm, curr, temp, step = max(mxm, curr + temp), arr[i - 1], k, 0
        mxm = max(mxm, curr + temp)
        if mxm > sum(arr):
            mxm = sum(arr)
        return mxm
