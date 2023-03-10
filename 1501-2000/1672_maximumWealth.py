class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        rich = 0
        for account in accounts:
            rich = max(rich, sum(account))
        return rich
