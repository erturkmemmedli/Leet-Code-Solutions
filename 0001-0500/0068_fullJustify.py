class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        output = []
        covering_place = 0
        count_word = 0

        for i, word in enumerate(words):
            if covering_place + len(word) + count_word <= maxWidth:
                covering_place += len(word)
                count_word += 1
            else:
                space = maxWidth - covering_place
                if count_word > 1:
                    width, add = divmod(space, count_word - 1)
                    string = ""

                    for j in range(i - count_word, i):
                        string += words[j]

                        if j != i - 1:
                            if add != 0:
                                string += " " * (width + 1)
                                add -= 1
                            else:
                                string += " " * width
                else:
                    string = words[i - 1] + " " * (maxWidth - len(words[i - 1]))
                    
                output.append(string)
                covering_place = len(word)
                count_word = 1

        string = ""

        for j in range(len(words) - count_word, len(words)):
            string += words[j]

            if j != len(words) - 1:
                string += " "

        string += " " * (maxWidth - len(string))
        output.append(string)

        return output
