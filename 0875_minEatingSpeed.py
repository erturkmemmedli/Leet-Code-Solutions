class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        remind = math.inf
        left = 1
        right = max(piles)
        while left <= right:
            mid = (left + right) // 2
            s = sum([math.ceil(pile / mid) for pile in piles])
            print(mid, s)
            if s > h:
                left = mid + 1
            elif s < h:
                right = mid - 1
            else:
                remind = min(remind, mid)
                right = mid - 1
        return remind if remind != math.inf else left

# Alternative solution

class Solution1:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right) // 2
            s = sum([math.ceil(pile / mid) for pile in piles])
            print(mid, s)
            if s > h:
                left = mid + 1
            else:
                right = mid
        return left
