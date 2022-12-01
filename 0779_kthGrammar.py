class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        queue = collections.deque()
        k -= 1
        while k > 0:
            queue.appendleft(k)
            k //= 2
        queue.appendleft(0)
        symbol = 0
        for i in range(1, len(queue)):
            if queue[i] == 2 * queue[i-1] + 1:
                symbol ^= 1
        return symbol

# Alternative solution (which gives TLE error)

class Solution1:
    def kthGrammar(self, n: int, k: int) -> int:
        table = [0]
        modifyingTable = []
        for _ in range(n-1):
            for i in table:
                if i:
                    modifyingTable.extend([1, 0])
                else:
                    modifyingTable.extend([0, 1])
            table = modifyingTable
            modifyingTable = []
        return table[k-1]
