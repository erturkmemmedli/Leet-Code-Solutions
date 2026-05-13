class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return
        c = Counter()
        for i in range(len(s) - 9):
            c[s[i:i+10]] += 1
        answer = []
        for key, val in c.items():
            if val > 1:
                answer.append(key)
        return answer

# Alternative solution

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hashmap = defaultdict(int)
        for i in range(0, len(s) - 9):
            hashmap[s[i:i+10]] += 1
        return [k for k, v in hashmap.items() if v > 1]

# Alternative solution

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequence_counter = defaultdict(int)
        dna_map = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        rabin_karp_map = {}
        output = []
        hash_val = 0

        for i in range(len(s)):
            if i < 10:
                hash_val = 4 * hash_val + dna_map[s[i]]
                if i == 9:
                    rabin_karp_map[hash_val] = s[:10]
                    sequence_counter[hash_val] += 1
            else:
                hash_val = 4 * (hash_val - dna_map[s[i-10]] * 4**9) + dna_map[s[i]]
                if hash_val not in rabin_karp_map:
                    rabin_karp_map[hash_val] = s[i-9:i+1]
                sequence_counter[hash_val] += 1
                if sequence_counter[hash_val] == 2:
                    output.append(rabin_karp_map[hash_val])

        return output
