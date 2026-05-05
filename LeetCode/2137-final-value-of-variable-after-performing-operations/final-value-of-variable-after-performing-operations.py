class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0
        for oper in operations:
            if "+" in oper:
                ans += 1
            elif "-" in oper:
                ans -= 1
        
        return ans