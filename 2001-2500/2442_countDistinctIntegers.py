class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n = [str(i) for i in nums]
        n = set(n)
        l = len(n)
        v = set()
        for i in n:
            r = i[::-1]
            if r[0] == '0':
                r = r.lstrip('0')
            if r not in n:
                v.add(r)
        return l + len(v)
