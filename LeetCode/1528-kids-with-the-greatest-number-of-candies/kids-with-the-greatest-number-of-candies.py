class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        current_greatest = max(candies)
        ans = []

        for kid in candies:
            kid += extraCandies
            if kid >= current_greatest:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans