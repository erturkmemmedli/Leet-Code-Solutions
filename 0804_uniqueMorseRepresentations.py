import string

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mors_set = set()
        mors_code = [".-","-...","-.-.","-..",".","..-.","--.", "....","..",".---","-.-",".-..","--","-.",
                     "---",".--.","--.-",".-.","...","-","..-", "...-",".--","-..-","-.--","--.."]
        alphabet = list(string.ascii_lowercase)
        mors_dict = dict(zip(alphabet, mors_code))
        converted = ''
        for word in words:
            for letter in word:
                converted += mors_dict[letter]
            mors_set.add(converted)
            converted = ''
        return len(mors_set)
