class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        while senate:
            c = collections.Counter(senate)
            if len(c) == 1:
                return "Radiant" if "R" in c else "Dire"
            senate, radiant, dire = self.vote(senate)
            if radiant:
                if radiant >= c["D"]:
                    return "Radiant"
                else:
                    temp = []
                    for party in senate:
                        if radiant and party == "D":
                            radiant -= 1
                        else:
                            temp.append(party)
                    senate = temp
            if dire:
                if dire >= c["R"]:
                    return "Dire"
                else:
                    temp = []
                    for party in senate:
                        if dire and party == "R":
                            dire -= 1
                        else:
                            temp.append(party)
                    senate = temp

    def vote(self, senate):
        def helper(candidate, first, second):
            if first > 0:
                first -= 1
            else:
                stack.append(candidate)
                second += 1
            return first, second
        stack = []
        radiant = 0
        dire = 0
        for party in senate:
            if not stack or party == stack[-1]:
                if party == "R":
                    radiant += 1
                if party == "D":
                    dire += 1
                stack.append(party)
            else:
                if party == "R":
                    dire, radiant = helper(party, dire, radiant)
                if party == "D":
                    radiant, dire = helper(party, radiant, dire)
        return stack, radiant, dire

# Alternative solution

class Solution1:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = collections.deque()
        dire = collections.deque()
        for i, party in enumerate(senate):
            if party == 'R':
                radiant.append(i)
            if party == 'D':
                dire.append(i)
        n = len(senate)
        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()
            if r < d:
                radiant.append(n + r)
            else:
                dire.append(n + d)
        return "Radiant" if radiant else "Dire"
