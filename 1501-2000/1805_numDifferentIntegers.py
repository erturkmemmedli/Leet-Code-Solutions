class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        string = ""
        result_set = set()

        for char in word:
            if char.isdigit():
                string += char
            else:
                if string:
                    result_set.add(int(string))
                string = ""
            
        if string:
            result_set.add(int(string))
            
        return len(result_set)
