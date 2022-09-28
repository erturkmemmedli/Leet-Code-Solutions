class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        if len(s1) != len(s2):
            return -1
        hashmap = {('x','y'): 0, ('y','x'): 0}
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                hashmap[(s1[i],s2[i])] += 1
        a = hashmap[('x','y')]
        b = hashmap[('y','x')]
        if (a + b) % 2 == 1:
            return -1
        return a//2 + b//2 + a%2 + b%2
