class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum=0
        total=0
        for i in accounts:
            total=sum(i)
            maximum=max(maximum,total)
        return maximum

        