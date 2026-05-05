class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        ans = 0

        for employee in hours:
            if employee < target:
                continue
            ans += 1
        
        return ans