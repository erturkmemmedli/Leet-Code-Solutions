class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        output = set()
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if len(words[j]) < len(words[i]):
                    if words[j] in words[i]:
                        output.add(words[j])
                else:
                    if words[i] in words[j]:
                        output.add(words[i])
        return output

# Alternative solution

class Solution1:
    def stringMatching(self, words):
        words = sorted(words, key = len)
        KMP_dict = {}
        for i in range(len(words)-1):
            KMP_dict["-" + words[i]] = self.KMP_values(words[i])
        output = set()
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if self.KMP_algo("-" + words[i], words[j], KMP_dict):
                    output.add(words[i])
        return output
                    
    def KMP_algo(self, pattern, string, dictionary):
        i, j = 0, 0
        while i < len(string) and j < len(pattern)-1:
            if string[i] == pattern[j+1]:
                i += 1
                j += 1
            elif j != 0:
                j = dictionary[pattern][j]
            else:
                i += 1
        if j == len(pattern)-1:
            return True
        
    def KMP_values(self, pattern):
        p, i, j = [0, 0], 0, 1
        while j < len(pattern):
            if pattern[j] == pattern[i]:
                p.append(p[-1] + 1)
                i += 1
                j += 1
            else:
                p.append(0)
                j += 1
        return p

# Alternative solution

class Solution2:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key = len)
        output = []
        for i in range(len(words)-1):
            string = "-".join(words[i:])
            if self.KMP(string, words[i]):
                output.append(words[i])
        return output
        
    def KMP(self, string, pattern):
        s = len(string)
        p = len(pattern)
        kmp = [0] * s
        for i in range(1, s):
            j = kmp[i-1]
            while 0 < j < p and string[i] != pattern[j]:
                j = kmp[j-1]
            if j == p:
                j = kmp[j-1]
            if string[i] == pattern[j]:
                j += 1
            kmp[i] = j
            if kmp[-1] == p: return True
        return kmp.count(p)
