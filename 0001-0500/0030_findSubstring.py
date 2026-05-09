class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_map = Counter(words)
        lenght_of_permutation = len(words[0]) * len(words)
        word_length = len(words[0])
        output = []

        for i in range(len(s) - lenght_of_permutation + 1):
            j = i
            temp_map = word_map.copy()
            string = ""

            while j < i + lenght_of_permutation:
                while len(string) < word_length:
                    string += s[j]
                    j += 1
                
                if string in temp_map:

                    temp_map[string] -= 1

                    if temp_map[string] == 0:
                        del temp_map[string]

                    if not temp_map:
                        output.append(i)

                    string = ""
                else:
                    string = ""
                    break
    
                string = ""
            
        return output

# Alternative solution

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        window = Counter(words)
        total = sum(len(w) for w in words)
        k = len(words[0])
        output = []
        successful_visits = set()
        unsuccessful_visits = set()
        for i in range(len(s) - total + 1):
            new_check = s[i:i+total]
            if new_check in successful_visits:
                output.append(i)
                continue
            elif new_check in successful_visits:
                continue
            j = i
            temp = window.copy()
            string = ""
            while j < i + total:
                while len(string) < k:
                    string += s[j]
                    j += 1
                if string in temp:
                    temp[string] -= 1
                    if temp[string] == 0:
                        del temp[string]
                    if not temp:
                        successful_visits.add(new_check)
                        output.append(i)
                    string = ""
                else:
                    string = ""
                    unsuccessful_visits.add(new_check)
                    break
                string = ""
        return output
