class TrieNode:
    def __init__(self):
        self.one = None
        self.zero = None

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = TrieNode()
        for num in nums:
            node = root
            for i in range(31,-1,-1):
                temp = num & 1 << i
                if temp:
                    if not node.one:
                        node.one = TrieNode()
                    node = node.one
                else:
                    if not node.zero:
                        node.zero = TrieNode()
                    node = node.zero
        answer = 0
        for num in nums:
            node = root
            value = 0
            for i in range(31,-1,-1):
                temp = num & 1 << i
                if node.one and not temp:
                    node = node.one
                    value += 1 << i
                elif node.zero and temp:
                    node = node.zero
                    value += 1 << i
                else:
                    node = node.one or node.zero
            answer = max(answer, value)
        return answer
