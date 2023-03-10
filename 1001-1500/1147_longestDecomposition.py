from collections import deque as Q

class Solution:
    def longestDecomposition(self, text: str) -> int:
        count, i, j = 0, 0, len(text) - 1
        head, tail = Q(), Q()
        while i <= j:
            head.append(text[i])
            tail.appendleft(text[j])
            if i == j:
                count += 1
                break
            if head == tail:
                count += 2
                head, tail = Q(), Q()
            elif 0 <= j - i <= 2:
                count += 1
                break
            i += 1
            j -= 1
        return count
