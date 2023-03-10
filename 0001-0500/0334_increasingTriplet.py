class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        dp = []
        for num in nums:
            index = bisect.bisect_left(dp, num)
            if index == len(dp):
                dp.append(num)
            else:
                dp[index] = num
            if len(dp) == 3:
                return True
        return False
        
# Alternative solution

class Solution1:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a, b, c = None, None, None
        for num in nums:
            if a == None:
                a = num
            elif b == None:
                if num <= a:
                    a = num
                else:
                    b = num
            elif c == None:
                if num <= a:
                    a = num
                elif num <= b:
                    b = num
                else:
                    return True
        return False
