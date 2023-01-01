class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k != 1:
            return "".join(sorted(s))
        mini, curr, idx, count, size, head = '~', -1, -1, 0, 0, True
        for i, char in enumerate(s):
            if char < mini:
                mini = char
                idx = i
                curr = i
                count = 1
                size = 1
                head = False
            elif char == mini:
                count += 1
                if head:
                    curr = i
                    head = False
                    if size != 1:
                        continue
                if count > size:
                    size = count
                    idx = curr
                elif count == size:
                    print(idx, curr)
                    k = 0
                    while s[(idx + size + k) % len(s)] == s[(curr + size + k) % len(s)]:
                        k += 1
                    if s[(idx + size + k) % len(s)] > s[(curr + size + k) % len(s)]:
                        idx = curr
            else:
                count = 0
                head = True
        s = s[idx:] + s[:idx]
        return s
