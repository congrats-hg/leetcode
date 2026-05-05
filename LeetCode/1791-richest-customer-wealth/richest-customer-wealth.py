class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        total_lst = []

        for customer in accounts:
            total_amount = sum(customer)
            total_lst.append(total_amount)
        
        ans = max(total_lst)
        
        return ans