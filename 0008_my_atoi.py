class Solution:
    def myAtoi(self, s: str) -> int:
        parse = ''
        negative_flag = False
        positive_flag = False
        for i in range(len(s)):
            if s[i] == ' ':
                if len(parse) == 0 and negative_flag == False and positive_flag == False:
                    continue
                else:
                    break
            elif s[i] == '+':
                if len(parse) == 0 and negative_flag == False and positive_flag == False:
                    positive_flag = True
                    continue
                else:
                    break
            elif s[i] == '-':
                if len(parse) == 0 and negative_flag == False and positive_flag == False:
                    negative_flag = True
                    continue
                else:
                    break
            elif s[i] in '0123456789':
                parse += s[i]
            else:
                break
        if len(parse) == 0:
            return 0
        if not negative_flag:
            return 2 ** 31 - 1 if int(parse) > 2 ** 31 - 1 else int(parse)
        else:
            return - 2 ** 31 if int(parse) > 2 ** 31 else -1 * int(parse)