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
