class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        upper = max(nums) + 1
        mod = 1_000_000_007

        prime = [1] * upper
        prime[0] = prime[1] = 0
        prime_score = [0] * upper

        for i in range(2, upper):
            if prime[i]:
                for j in range(i, upper, i):
                    prime_score[j] += 1
                    prime[j] = 0

        next_gr_element = [n] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and prime_score[nums[i]] >= prime_score[nums[stack[-1]]]:
                stack.pop()

            next_gr_element[i] = stack[-1] if stack else n
            stack.append(i)
        
        prev_ge_element = [-1] * n
        stack = []

        for i in range(n):
            while stack and prime_score[nums[i]] > prime_score[nums[stack[-1]]]:
                stack.pop()

            prev_ge_element[i] = stack[-1] if stack else -1
            stack.append(i)

        score = 1
        tuples = [(nums[i], i) for i in range(n)]
        tuples.sort(reverse=True)

        def power(num, ops):
            result = 1

            while ops > 0:
                if ops % 2 == 1:
                    result = (result * num) % mod
                
                num = (num ** 2) % mod
                ops //= 2

            return result

        for num, idx in tuples:
            operations = min((idx - prev_ge_element[idx]) * (next_gr_element[idx] - idx), k)
            score = (score * power(num, operations)) % mod
            k -= operations

            if k == 0:
                return score

        return score
