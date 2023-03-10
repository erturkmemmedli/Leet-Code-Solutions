class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        address = set()
        for email in emails:
            temp = ""
            flag = False
            for i, char in enumerate(email):
                if char == '.':
                    continue
                if char == '+':
                    flag = True
                if char == '@':
                    temp += email[i:]
                    break
                if not flag:
                    temp += char
            address.add(temp)
        return len(address)

# Alternative solution

class Solution1:
    def numUniqueEmails(self, emails: List[str]) -> int:
        address = set()
        for email in emails:
            at = email.index('@')
            try:
                plus = email.index('+')
            except:
                plus = None
            try:
                period = email.index('.')
            except:
                period = None
            while period != None and period < at:
                if plus != None:
                    if period < plus:
                        plus -= 1
                    else:
                        break
                email = email[:period] + email[period+1:]
                at -= 1
                try:
                    period = email.index('.')
                except:
                    period = None
            if plus != None:
                email = email[:plus] + email[at:]
            address.add(email)
        return len(address)
