class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        judge = {}
        for a, b in trust:
            if b not in judge:
                judge[b] = [a]
            else:
                judge[b].append(a)
        mxm = 0
        J = n
        for k, v in judge.items():
            if len(v) > mxm:
                mxm = len(v)
                J = k
        if not judge:
            if J == 1:
                return J
            return -1
        if len(judge[J]) < n-1:
            return -1
        for k, v in judge.items():
            if k == J:
                continue
            if J in v:
                return -1
        return J
      
# Alternative solution

class Solution1:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust:
            if n == 1:
                return n
            return -1
        judge = {}
        for a, b in trust:
            if b not in judge:
                judge[b] = [a]
            else:
                judge[b].append(a)
        j = max(judge.values(), key = len)
        if len(j) < n-1:
            return -1
        for k, v in judge.items():
            if v == j:
                J = k
                break
        for k, v in judge.items():
            if k == J:
                continue
            if J in v:
                return -1
        return J
