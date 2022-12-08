class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        costs = []
        for i in range(len(s)):
            costs.append(abs(ord(s[i]) - ord(t[i])))
        window = collections.deque()
        maxLength = 0
        total = 0
        for cost in costs:
            while window and total + cost > maxCost:
                pop = window.popleft()
                total -= pop
            if total + cost <= maxCost:
                total += cost
                window.append(cost)
            maxLength = max(maxLength, len(window))
        return maxLength
